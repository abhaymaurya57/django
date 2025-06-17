from django.urls import path
from . import views

urlpatterns = [
   path('',views.students, name='students'),  # This will map the root URL of the student app to the students view
]