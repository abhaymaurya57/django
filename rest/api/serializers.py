from rest_framework import serializers
from student.models import Student
from employees.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        
class StudentSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Student
        fields = "__all__"