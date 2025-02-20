from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static  


urlpatterns = [  
    # path('',views.base,name='base'),
    path('',views.home, name='home'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signin'),
    path('about/',views.about,name='about'),
    path('signin/',views.signin,name='signin'),
    path('skill/',views.skill,name='skill'),

]