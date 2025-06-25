from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegisterView
from .views import (
    RegisterAdminView, RegisterStaffView, RegisterStudentView,
    AdminLoginView, StaffLoginView,StudentLoginView, StaffLoginView,AdminLoginView,studentformregister,
    StudentListCreateAPIView,StudentRetrieveUpdateDestroyAPIView,
)
from .views import StudentLogin

urlpatterns = [
    # Page Routes
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('', views.base, name='base'),
    path('adminn/login/', views.adminlogin, name='admin_login'),
    path('staff/login/', views.stafflogin, name='staff_login'),
    path('student/login/', views.StudentLogin, name='student_login'),
    path('adminndashboard/', views.admindashboard, name='admin_dashboard'),
    path('staff/dashboard/', views.staffdashboard, name='staff_dashboard'),
    path('student/dashboard/', views.studentform, name='student_dashboard'),

    # API Routes
    path('api/login/admin/', views.AdminLoginView.as_view(), name='admin_login_api'),
    path('api/staff-login/', views.StaffLoginView.as_view(), name='staff_login_api'),
    path('api/student-login/', views.StudentLoginView.as_view(), name='student_login_api'),
    path('api/student-form/', views.studentformregister.as_view(), name='student_form_api'),

    # Registration
    path('api/register-admin/', views.RegisterAdminView.as_view(), name='register_admin'),
    path('api/register-staff/', views.RegisterStaffView.as_view(), name='register_staff'),
    path('api/register-student/', views.RegisterStudentView.as_view(), name='register_student'),

    #admin edit and delete 
    path('api/students/', StudentListCreateAPIView.as_view(), name='student_list_create'),
    path('api/students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student_detail'),
   
    #student profile
    path('api/student-profile/', views.StudentProfileAPIView.as_view(), name='student_profile_api'),
    path('profile/', views.student_profile_page, name='student_profile_page'),

]
