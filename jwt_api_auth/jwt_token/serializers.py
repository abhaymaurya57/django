from rest_framework import serializers
from .models import MyUser,Student,Staff,StudentRegistr,MyUser
from django.contrib.auth import authenticate


class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['userid', 'email', 'name', 'phonenumber', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data, role='admin')


class StaffRegistrationSerializer(serializers.ModelSerializer):
    department = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ['userid', 'email', 'name', 'phonenumber', 'password', 'department']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        department = validated_data.pop('department')
        user = MyUser.objects.create_user(**validated_data, role='staff')
        Staff.objects.create(user=user, department=department)
        return user


class StudentRegistrationSerializer(serializers.ModelSerializer):
    roll_no = serializers.CharField(required=True)

    class Meta:
        model = MyUser
        fields = ['userid', 'email', 'name', 'phonenumber', 'password', 'roll_no']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        roll_no = validated_data.pop('roll_no')
        user = MyUser.objects.create_user(**validated_data, role='student')
        Student.objects.create(user=user, roll_no=roll_no)
        return user



class LoginSerializer(serializers.Serializer):
    userid = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        userid = data.get('userid')
        password = data.get('password')
        user = authenticate(userid=userid, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data

class studentformserializer(serializers.ModelSerializer):
    class Meta:
        model=StudentRegistr
        fields="__all__"
    

