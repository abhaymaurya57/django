from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    AdminRegistrationSerializer,
    StaffRegistrationSerializer,
    StudentRegistrationSerializer,
    LoginSerializer,
    studentformserializer,StudentSerializer,StudentSerializer
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import StudentRegistr
from django.shortcuts import get_object_or_404

#  Base View
def base(request):
    return render(request, 'base.html')


#  Registration Page Template
class UserRegisterView(APIView):
    def get(self, request):
        return render(request, "registation.html")

    def post(self, request):
        return Response({"message": "User registered"})


#  Token Generator
def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


#  Admin Registration
class RegisterAdminView(APIView):
    def post(self, request):
        serializer = AdminRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Admin registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Staff Registration
class RegisterStaffView(APIView):
    def post(self, request):
        serializer = StaffRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Staff registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Student Registration
class RegisterStudentView(APIView):
    def post(self, request):
        serializer = StudentRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Student registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  Admin Login (NO authentication_classes here)
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


#  Staff Login
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


# Student Login
class StudentLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if user.role != 'student':
                return Response({'detail': 'Not a student account'}, status=status.HTTP_403_FORBIDDEN)
            tokens = get_tokens_for_user(user)
            return Response(tokens, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


# Student Dashboard Template View
def studentform(request):
    return render(request, "std_dash_base.html")


# Submit Student
class studentformregister(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'student':
            return Response({'detail': 'Unauthorized'}, status=403)

        data = request.data.copy()
        data['email'] = request.user.email  # ✅ auto-link by email
        serializer = studentformserializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Student registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Admin Dashboard
def admindashboard(request):
    users=StudentRegistr.objects.all()
    return render(request, "admin_dashboard.html",{"users":users})


# Staff Dashboard
def staffdashboard(request):
    return render(request, "staff_dashboard.html")


#  Student Login Page
def StudentLogin(request):
    return render(request, "student_login.html")


#  Admin Login Page
def adminlogin(request):
    return render(request, "admin_login.html")


# Staff Login Page
def stafflogin(request):
    return render(request, "staff_login.html")

class StudentListCreateAPIView(APIView):
    def get(self, request):
        students = StudentRegistr.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        student = get_object_or_404(StudentRegistr, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = get_object_or_404(StudentRegistr, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = get_object_or_404(StudentRegistr, pk=pk)
        student.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_204_NO_CONTENT)
    
def student_profile_page(request):
    return render(request, "profile.html")

class StudentProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        student_data = StudentRegistr.objects.filter(email=request.user.email).first()
        if not student_data:
            return Response({'detail': 'No profile data found'}, status=404)
        serializer = StudentSerializer(student_data)
        return Response(serializer.data)
