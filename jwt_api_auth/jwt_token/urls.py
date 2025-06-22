from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegisterView
from .views import (
    RegisterAdminView, RegisterStaffView, RegisterStudentView,
    AdminLoginView, StaffLoginView,StudentLoginView, StaffLoginView,AdminLoginView,studentformregister
)
from .views import StudentLogin

urlpatterns = [

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #templates of base page
    path("",views.base,name="base"),

    #Student Admin Staff register
    path('register/', UserRegisterView.as_view(), name='register'),

    # templates of login
    path('student/login/', views.StudentLogin, name='student_login'),
    path('staff/login/', StaffLoginView.as_view(), name='staff_login'),
    path("adminn/login/", views.adminlogin,name='adminlogin'),

    #serilizers and views
    path('api/register/admin/', RegisterAdminView.as_view(), name='register_admin'),
    path('api/register/staff/', RegisterStaffView.as_view(), name='register_staff'),
    path('api/register/student/', RegisterStudentView.as_view(), name='register_student'),
     path('api/register-student/', studentformregister.as_view(), name='api-register-student'),

    # Login Endpoints
    path('api/login/admin/', AdminLoginView.as_view(), name='login_admin'),
    path('api/login/staff/', StaffLoginView.as_view(), name='login_staff'),
    path('api/login/student/', StudentLoginView.as_view(), name='login_student'),

    #dashboard templates
    path('student/dashboard/',views.studentform,name='studentdashboard'),
    path('adminn/dashboard/',views.admindashboard,name="admindashboard"),
]
