from . import models
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Teacher
        field = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        models=models.Subject
        field='__all__'