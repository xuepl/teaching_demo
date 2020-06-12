from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from api import models
from . import serializers
from  utils.custome_response import CustomeResponse


class Messages(generics.GenericAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.ModelSerializerMessage

    def post(self,request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return CustomeResponse(serializer.validated_data,code='0000',msg="新增成功")

