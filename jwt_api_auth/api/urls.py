from django.urls import path
from . import views
urlpatterns = [
    path("std/",views.StudentRegister.as_view(),name="studentregister"),
    path("cource/",views.courceregister.as_view(),name="courceregister"),
    path('stud/',views.student_api),
    path('stud/<int:pk>/',views.student_api),
    path('authors/', views.AuthorCreateView.as_view(), name='author-create'),
]
