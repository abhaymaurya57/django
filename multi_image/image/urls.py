from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name='base'),
    path('images/',views.images,name='images'),
    path('upload/',views.upload,name='upload'),
    path('delete/', views.delete, name='delete'),

]