from .models import Student
from .serializers import StudentSerilizers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


class StudentModelViewsSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
