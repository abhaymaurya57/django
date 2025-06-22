from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import AdminRegistrationSerializer, StaffRegistrationSerializer, StudentRegistrationSerializer
from .serializers import LoginSerializer,studentformserializer
from rest_framework.permissions import IsAuthenticated

def base(request):
   return render(request,'base.html')

class UserRegisterView(APIView):
    def get(self, request):
        return render(request, "registation.html") 

    def post(self, request):
        return Response({"message": "User registered"})
    

def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterAdminView(APIView):
    def post(self, request):
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Admin registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterStaffView(APIView):
    def post(self, request):
        serializer = StaffRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Staff registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def adminlogin(request):
    return render(request,"admin_login.html")

def admindashboard(request):
    return render(request,"admin_dashboard.html")
    
class AdminLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user.role != 'admin':
                return Response({'detail': 'Not an admin account'}, status=status.HTTP_403_FORBIDDEN)
            tokens = get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class StaffLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user.role != 'staff':
                return Response({'detail': 'Not a staff account'}, status=status.HTTP_403_FORBIDDEN)
            tokens = get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class RegisterStudentView(APIView):
    def post(self, request):
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Student registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

def StudentLogin(request):
    return render(request,"student_login.html")

class StudentLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user.role != 'student':
                return Response({'detail': 'Not a student account'}, status=status.HTTP_403_FORBIDDEN)
            tokens = get_tokens_for_user(user)
            print(tokens)
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

def studentform(request):
    return render(request,"std_dash_base.html")

class studentformregister(APIView):
    # permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = studentformserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)