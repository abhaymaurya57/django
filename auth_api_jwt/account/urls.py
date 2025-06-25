from django.urls import path
from account.views import UserRegistationView,UserLoginView,UserProfileView,UserChangePassword,SendPasswordResetEmailView,UserPasswordResetView
from .views import register_template_view, login_template_view
from .views import *

urlpatterns = [
    path('register/',UserRegistationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('change/',UserChangePassword.as_view(),name='changepassword'),
    path('sent_reset_password_email/',SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name="reset_password"),
    
    # frontent connect backend

    path("",base,name='base'),
    path('register-form/', register_template_view, name='register-form'),
    path('login-form/', login_template_view, name='login-form'),
    path('profile-temp/', profile_template_view, name='profile'),
    path('change-password/', change_password_view, name='change-password'),
    path('send-reset-email/', send_reset_email_view, name='send-reset-email'),
    path('reset-password/<uid>/<token>/', reset_password_template_view, name='reset-password'),

    # path('dashboard/', dashboard_view, name='dashboard')
    path('admin-dashboard/', admin_dashboard_view, name='admin-dashboard'),
    path('staff-dashboard/', staff_dashboard_view, name='staff-dashboard'),
    path('user-dashboard/', user_dashboard_view, name='user-dashboard'),

    path('courses/', CourseListAPI.as_view(), name='course-list'),
    path('students/', StudentCreateAPI.as_view(), name='student-create'),
]