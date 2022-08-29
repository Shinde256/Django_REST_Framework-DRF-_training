from django.shortcuts import render
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView
from .models import Student
from .mypaginations import mypagenumber

class StudentListViews(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class = mypagenumber




