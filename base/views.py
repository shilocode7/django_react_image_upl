from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from rest_framework.response import Response
# Create your views here.
from rest_framework import serializers , status


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
   
@api_view(['GET']) 
def index(request):
    return Response("hello")

@api_view(['GET','POST',"DELET","PUT"])
def student(request,id=-1):
    if request.method =="GET":
        if int(id) > -1: #get singl student
            try:
                my_model=Student.objects.get(id=int(id))
            except:
                return Response("not exist")
            serializer = StudentSerializer(my_model, many=False)
        else:
            my_model = Student.objects.all()
            serializer = StudentSerializer(my_model, many=True)
        return Response(serializer.data)
    if request.method == 'DELETE':
        if int(id) > -1:
            stu_2_del=Student.objects.get(id=int(id))
            stu_2_del.delete()
            return Response(f"Student deleted id:{id}")
    if request.method == 'PUT':
        if int(id) > -1:
            my_models = Student.objects.get(id=int(id))
            serializer = StudentSerializer(my_models,data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response("students" +request.method)
