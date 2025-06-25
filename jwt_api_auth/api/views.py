      
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import courseregisterserializers,StudentRegisterSerializer,studentserializer,AuthorSerializer
from .models import student,Cource,Stud
from rest_framework.decorators import api_view

class StudentRegister(APIView):
    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Data is saved", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error": "Invalid data", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class courceregister(APIView):
    def post(self,request):
        serializer=courseregisterserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"messege":"ok save data","data":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"something is wrong","data":serializer.error},status=status.HTTP_400_BAD_REQUEST)
        
        #function base

  
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_api(request,pk=None):
    if request.method=='GET':
        if pk is not None: 
            std = Stud.objects.get(pk=pk)
            serializer = studentserializer(std)
            return Response(serializer.data)
        std = Stud.objects.all()
        serializer = studentserializer(std,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)

    if request.method=='DELETE':
        stu = Stud.objects.get(pk=pk)
        stu.delete()
        return Response({"msg": "data deleted"})
    

    if request.method=='PUT':
        stu = Stud.objects.get(pk=pk)
        serializer =studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
    return Response(serializer.errors)  


#************** Author serializers  API view ******************

class AuthorCreateView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Author and books created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)