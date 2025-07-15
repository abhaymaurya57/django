from django.urls import path,include
from . import views
urlpatterns = [
    path('',include('middlewareapp.urls')),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
]