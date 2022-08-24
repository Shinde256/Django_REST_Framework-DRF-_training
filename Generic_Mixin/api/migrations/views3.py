from .models import Student
from .serializers import StudentSerilizers

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView

class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
class StudentList(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
class StudentList(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
class StudentList(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
