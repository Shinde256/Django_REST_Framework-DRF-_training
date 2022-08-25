from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerilizers

@api_view(['GET','PUT','POST','DELETE'])
def stundet_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = StudentSerilizers(stu)
            return Response(serializers.data)
        stu = Student.objects.all()
        serializers = StudentSerilizers(stu,many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        serilizer = StudentSerilizers(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data created'})
        return Response(serilizer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk = id)
        serializers =StudentSerilizers(stu,data=request.data , partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data updated'})
        return Response(serializers.errors)

    if request.method == 'DELETE':
        id = request.data.get ('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data Deleted'})



