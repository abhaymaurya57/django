from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer,SubjectSerializer
from .models import Teacher,Subject
from . import models
# Create your views here.
class TeacherViewset(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class subjectviewset(viewsets.ModelViewSet):
    serializer_class=SubjectSerializer
    queryset= Subject.objects.all()
