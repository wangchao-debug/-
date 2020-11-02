
from rest_framework import serializers, exceptions

from api.models import Employee
from drf_day2 import settings


class EmployeeSerializer(serializers.Serializer):
    """
    定义序列化器类，写需要为每一个model去编写对应的序列化器类
    """
    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()
    # gender = serializers.IntegerField()

    aaa = serializers.SerializerMethodField()
    def get_aaa(self,obj):
        return "牛逼"

    gender = serializers.SerializerMethodField()
    def get_gender(self,obj):
        # gender值时choices类型 get_字段名_display直接访问值
        # print(obj.get_gender_display())
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()
    def get_pic(self,obj):
        # print("http://127.0.0.1:8000/"+settings.MEDIA_URL+str(obj.pic))
        return "%s%s%s"%("http://127.0.0.1:8000/",settings.MEDIA_URL,str(obj.pic))


class StudentSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class EmployeeDeSerializer(serializers.Serializer):
    """
    反序列化器作用：将前端提交的数据保存到数据库
    1. 需要前端提供那些字段
    2. 对字段进行安全校验
    3. 有没有字段需要额外的校验
    反序列化不需要自定义字段
    """
    # 添加校验规则
    username = serializers.CharField(
        max_length=100,
        min_length=2,
        error_messages={
            "max_length":"长度太长了",
            "min_length":"长度太短了"
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField()
    re_pwd = serializers.CharField()
    # def get_re_pwd(self,obj):
    #     return "123456"

    # TODO 钩子函数，在create方法执行之前，DRF提供了两个钩子函数来对数据进行校验

    # 全局钩子
    def validate(self, attrs):
        print(attrs)
        pwd = attrs.get("password")
        print(pwd)
        re_pwd = attrs.pop("re_pwd")
        print(re_pwd)
        if pwd !=re_pwd:
            raise exceptions.ValidationError("两次输入的密码不一致")
        return attrs
    #
    # 局部钩子
    def validate_username(self,value):
            # 自定义用户名的校验规则
            # print(value)
            if "1" in value:
                # print("用户名有误")
                raise exceptions.ValidationError("用户名中不能包含1")
            emp = Employee.objects.filter(username=value)
            if emp:
                raise exceptions.ValidationError("用户名已存在")
            return value

    # 如果想要完成对象的新增，必须重写create()方法
    # self是序列化器对象，validated_data是需要保存的数据
    def create(self, validated_data):
        # print("33333")
        # print(self)
        # print(validated_data)
        return Employee.objects.create(**validated_data)