from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('excp/',excp,name='home'),
    path('user/',user_info,name='user')

]
