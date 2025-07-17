from django.urls import path
from cacheapp import views
urlpatterns = [
   path('',views.home)
]
