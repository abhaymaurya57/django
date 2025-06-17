from django.urls import path
from account.views import UserRegistationView,UserLoginView,UserProfileView,UserChangePassword,SendPasswordResetEmailView,UserPasswordResetView


urlpatterns = [
    path('register/',UserRegistationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('change/',UserChangePassword.as_view(),name='changepassword'),
    path('sent_reset_password_email/',SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name="reset_password")
]