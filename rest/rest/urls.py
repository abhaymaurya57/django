from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # web application endpoint
    path('student/',include('student.urls')) ,
    path('employees/',include('employees.urls')) ,

    #Api endpoint
    path('api/v1/',include('api.urls')), 


]