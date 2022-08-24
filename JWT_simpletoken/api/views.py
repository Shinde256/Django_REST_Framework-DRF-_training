from .models import Student
from .serializers import StudentSerilizers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .customauth import CustomAuthentication


class StudentModelViewsSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
