
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerilizers
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request, pk = None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = StudentSerilizers(stu)
            return Response(serializers.data)
        stu = Student.objects.all()
        serializers = StudentSerilizers(stu, many=True)
        return Response(serializers.data)


    def post(self,request, format=None):
        serilizer = StudentSerilizers(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data created'})
        return Response(serilizer.errors)

    def put (self,request, format=None):
        id = request.data.get('id')
        stu = Student.objects.get(pk = id)
        serializers =StudentSerilizers(stu,data=request.data , partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'data updated'})
        return Response(serializers.errors)

    def delete(self,request,pk=None,format= None):
        id = pk
        st = request.data.get (pk = id)
        stu = Student.objects.get(st)
        stu.delete()
        return Response({'msg':'data Deleted'})

    def patch(self, request,pk=None, format= None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializers = StudentSerilizers(stu,data=request.data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'partial data updated'})
        return Response(serializers.errors)



