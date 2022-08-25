from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        if id is not None:
            stu = Student.objects.get(id =id)
            serializer= StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data , content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializers = StudentSerializers(data=python_data)
        if serializers.is_valid():
            serializers.save()
            res = {'msg':' data created '}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer.render(serializers.errors)
        return HttpResponse (json_data,content_type='application.jason')

    if request.method == 'PUT':
        json_data = request.body
        steam = io.BytesIO(json_data)
        python_data = JSONParser().parse(steam)
        id = python_data.get('id')
        stud = Student.objects.get(id=id)
        serializers = StudentSerializers(stud ,data=python_data, partial=True)
        if serializers.is_valid():
            serializers.save()
            res = {'msg': 'Data updated !!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse (json_data,content_type='application.json')
        json_data = JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data, content_type='application.json')

    if request.method =="DELETE":
        json_data = request.body
        strame = io.BytesIO(json_data)
        python_data = JSONParser().parse(strame)
        id = python_data.get('id')
        stud =  Student.objects.get(id=id)
        stud.delete()
        res = {'msg':'data deleted'}
        json_data =JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')








