from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

class CustomAnonRateThrottle(UserRateThrottle):
    rate='3/day'

class StudentModelViewSet(viewsets.ModelViewSet):
    throttle_classes = [CustomAnonRateThrottle]
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class = StudentSerializer