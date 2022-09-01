from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']


