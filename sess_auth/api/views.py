from .models import Student
from .serializers import StudentSerilizers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions


class StudentModelViewsSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
