from django.urls import path
from . import views

urlpatterns = [
   path('students/',views.studentsview),
   path('students/<int:pk>/', views.studentDetailsview),
   path('employees/', views.Employees.as_view()),
   path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
]