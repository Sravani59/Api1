from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.
#serializer- It do both serialization and deserialization
#serialization- Convert orm to Json
#Deserialization- Convert Json to orm


class ProductCrud(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        JPO=ProductModelSerializer(PDO,many=True)
        return Response(JPO.data)
    
    def post(self,request):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'Insert':'Successfully'})
        else:
            return Response({'Error':'Not Inserted'})



