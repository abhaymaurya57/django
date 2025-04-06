from rest_framework import serializers
from .models import Person

class peopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        # exlude = ['name']
        # fields = ['name','age','a,']
        fields = '__all__'

    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError('age should be gretor than 18')
        return data

    # def validate_age(self, value):
    #     if value < 18:
    #         raise serializers.ValidationError("Age must be >= 18")
    #     return value
