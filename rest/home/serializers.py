from rest_framework import serializers
from .models import Person

class peopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        # exlude = ['name']
        # fields = ['name','age','a,']
        fields = '__all__'