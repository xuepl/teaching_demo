from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models

class ModelSerializerMessage(serializers.ModelSerializer):


    class Meta:
        model = models.Message
        fields="__all__"
        extra_kwargs = {
            "phone":{
                "validators":[UniqueValidator(queryset=models.Message.objects.all(),message="手机号已存在")]
            },
            "updatetime":{
                "read_only":True
            },
            "createtime": {
                "read_only": True
            }
        }