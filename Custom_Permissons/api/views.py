from .models import Student
from .serializers import StudentSerilizers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermisiions import My_Permissions


class StudentModelViewsSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [My_Permissions]
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
