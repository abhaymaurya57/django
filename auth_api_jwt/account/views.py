from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerilizer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer,UserPasswordResetSerializer
from django.contrib.auth import authenticate
from .renders import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from .models import User

# Create your views here.

def get_tokens_for_user(user):
    if not user.is_active:     
      raise AuthenticationFailed("User is not active")
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistationView(APIView):
    renderer_classes = [UserRenderer]
    print(renderer_classes)
    def post(self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            print(token)
            return Response({'token':token,'msg':'registation successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                # Role-based response
            if user.is_superuser:
                role = 'admin'
            elif user.is_staff:
                role = 'staff'
            else:
                role = 'user'

            return Response({'token': token, 'role': role, 'msg': 'Login successful'}, status=status.HTTP_200_OK)
                
        else:
            return Response({'error':{'non_field':['email and password is not valid']}},status=status.HTTP_404_NOT_FOUND)
            
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerilizer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserChangePassword(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data,
            context={'user': request.user}
        )
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password reset link send.plese check your email'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,uid,token,format=None):
        serializer = UserPasswordResetSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password reset successfully'},status=status.HTTP_200_OK)

from django.shortcuts import render

def register_template_view(request):
    return render(request, 'account/register.html')

def login_template_view(request):
    return render(request, 'account/login.html')

def profile_template_view(request):
    chais=User.objects.all()
    return render(request, 'account/base.html',{'chais': chais})

def change_password_view(request):
    return render(request, 'account/change_password.html')

def send_reset_email_view(request):
    return render(request, 'account/send_reset_email.html')
    
def reset_password_template_view(request, uid, token):
    return render(request, 'account/reset_password.html', {'uid': uid, 'token': token})

def admin_dashboard_view(request):
    return render(request, 'account/admin_dashboard.html')

def staff_dashboard_view(request):
    return render(request, 'account/staff_dashboard.html')

def user_dashboard_view(request):
    return render(request, 'account/user_dashboard.html')