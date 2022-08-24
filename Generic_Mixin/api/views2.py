from .models import Student
from .serializers import StudentSerilizers
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers

class StudentC(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers

class StudentR(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers

class StudentU(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers

class StudentD(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizers
