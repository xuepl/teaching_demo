from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=40, help_text="姓名")
    idcard = models.CharField(max_length=18, help_text="身份证号")
    phone = models.CharField(max_length=11, help_text="手机号", unique=True)
    email = models.EmailField(max_length=255, help_text="邮箱")
    age = models.IntegerField(help_text="姓名")
    address = models.CharField(max_length=255, null=True, blank=True, help_text="地址")
    updatetime = models.DateTimeField(auto_now=True, help_text="修改时间")
    createtime = models.DateTimeField(auto_now_add=True, help_text="创建日期")

    class Meta:
        db_table="message"



