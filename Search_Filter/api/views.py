from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [SearchFilter]
    search_fields =['city']
