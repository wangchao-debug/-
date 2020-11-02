from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework.response import Response

from app.models import User
from rest_framework.views import APIView

# @csrf_protect #在setting中注释掉全局csrf后，为某个视图单独添加csrf认证
@csrf_exempt #为某个视图免除csrf认证
def user(request):

    if request.method == "GET":
        username = request.GET.get("username")
        print(username)
        print("GET 查询")
        return HttpResponse("GET OK")

    if request.method == "POST":
        print("POST 新增")
        return HttpResponse("POST OK")
    if request.method == "PUT":
        print("PUT 修改")
        return HttpResponse("PUT OK")
    if request.method == "DELETE":
        print("DELETE 删除")
        return HttpResponse("DELETE OK")

"""
函数视图：function view 基于函数定义的视图
类视图：    class view      基于类定义的视图
"""

"""
单个：查询单个    查询所有    新增单个    删除单个    修改单个    局部修改单个
群体：新增单个     删除单个    修改多个    局部修改多个
"""
# 一个类里包含多个视图函数，通过请求方式匹配后端对应的方法
@method_decorator(csrf_exempt,name="dispatch")#为类视图免除csrf认证
# @method_decorator(csrf_protect,name="dispatch")#为类视图添加csrf认证
class UserView(View):
    def get(self,request,*args,**kwargs):
        """
        提供查询单个用户以及多个用户的接口
        :param request: 请求对象
        :param args:
        :param kwargs:
        :return:    返回查询结果
        """
        user_id = kwargs.get("id")
        if user_id:
            print(user_id)
            user_val = User.objects.filter(pk = user_id).values("username","password","gender").first()
            print(user_val)
            if user_val:
                # 如果查询出用户信息，则返回到前端
                return JsonResponse({
                    "status":200,
                    "message":"查询单个用户成功",
                    "results":user_val,
                })
            return JsonResponse({
                "status": 400,
                "message": "查询用户失败",
            })
        else:
            # 用户id不存在，则代表查询所有用户信息
            user_objects_all = User.objects.all().values("username","password","gender")
            print(user_objects_all)
            if user_objects_all:
                return JsonResponse({
                    "status":200,
                    "message":"查询所有用户成功",
                    "results":list(user_objects_all)
                })

    def post(self,request,*args,**kwargs):
        """
                新增单个用户
                """
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 200,
                "message": "新增单个用户成功",
                "result": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 400,
                "message": "新增单个用户失败",
            })

    def put(self,request,*args,**kwargs):
        print("PUT 删除")
        return HttpResponse("PUT OK")

    def delete(self,request,*args,**kwargs):
        print("DELETE 删除")
        return HttpResponse("DELETE OK")

class StudentAPIView(APIView):

    def get(self,request,*args,**kwargs):
        print("DRF GET VIEW")
        return Response("DRF GET OK")

    def post(self,request,*args,**kwargs):
        print("DRF POST VIEW")
        return Response("DRF POST OK")