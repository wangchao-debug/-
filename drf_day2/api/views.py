from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Student, Employee
from api.serializer import EmployeeSerializer, EmployeeDeSerializer


@method_decorator(csrf_exempt,name="dispatch")
class UserView(View):
    def get(self,request,*args,**kwargs):
        # print("get Success")
        # print(type(request))
        username = request.GET.get("username")
        print(username)
        return HttpResponse("GET OK")

    def post(self,request,*args,**kwargs):
        # print("post Success")
        email = request.POST.get("email")
        print(email)
        return HttpResponse("POST OK")

class StudentAPIView(APIView):

    def get(self,request,*args,**kwargs):
        print("get Success")
        print(type(request))
        email = request._request.GET.get("email")
        print(email)
        stu_id = kwargs.get("id")
        stu_obj = Student.objects.get(pk=stu_id)
        print(stu_obj)
        return Response("GET OK")



    def post(self,request,*args,**kwargs):
        # print("post Success")
        # WSGIrequest
        # email = request._request.POST.get("email")不推荐
        # restframework.views.Request
        email = request.POST.get("email")#这个request是drf中已经封装好的request（django的request）
        # print(email)
        # 通过DRF扩展的方式获取参数
        print(request.query_params)
        print(request.query_params.get("email"))
        # 可以获取前端传递的各种类型的参数，兼容性最强
        print(request.data.get("email"))#推荐用request.data获取值，除了GET请求外的其他请求方式，推荐用data
        return Response("POST OK")

class EmployeeAPIView(APIView):

    def get(self,request,*args,**kwargs):
        emp_id = kwargs.get("id")
        if emp_id:
            # 查询单个
            emp_obj = Employee.objects.get(pk=emp_id)
            emp_obj1 = Employee.objects.filter(pk=emp_id)
            # print(type(emp_obj))
            # print(emp_obj1)
            # .data将序列化器中的数据打包成字典返回
            employee = EmployeeSerializer(emp_obj).data
            # print(employee)
            return Response({
                "status":200,
                "message":"查询单个员工成功",
                "result":employee
            })
        else:
            employee_objects_all = Employee.objects.all()
            employee_all = EmployeeSerializer(employee_objects_all,many=True).data
            return Response({
                "status": 200,
                "message": "查询所有员工成功",
                "result": employee_all
            })

    def post(self,request,*args,**kwargs):
        request_data = request.data
        # print(request_data)
        if not isinstance(request_data,dict) or request_data =={}:
            return Response({
                "states": 400,
                "message": "参数有误"
            })
        # 使用序列化器完成数据库的反序列化
        # 在数据进行反序列化的时候需要指定关键字 data
        serializer = EmployeeDeSerializer(data=request_data)
        # print(serializer)
        # print("11111")
        # print(serializer.is_valid())
        # 需要对反序列化后的数据进行校验 通过is——valid()来对传递过来的参数进行校验    校验合法时，返回True
        if serializer.is_valid() :
            # 调用save()方法进行数据的保存 必须重写create()方法
            # print("222222")
            emp_ser = serializer.save()
            # print("444444")
            return Response({
                "states":200,
                "message":"员工添加成功",
                "result": EmployeeSerializer(emp_ser).data
            })
        else:
            return Response({
                "states": 400,
                "message": "员工添加失败",
                # 保存失败的信息会包含在 .errors中
                "result": serializer.errors
            })
        # print(serializer.is_valid())