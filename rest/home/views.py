from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import peopleSerializer
# Create your views here.
# person.object.all()
# [1,2,3,4] -> queryset



@api_view(['GET','POST','put'])
def index(request):  
    courses = {
        'course_name': 'python',  # <-- fixed spelling
        'learn': ['flask', 'Django', 'Tornado', 'fastapi'],
        'course_provider': 'scaler'  # <-- fixed spelling
    }
    if request.method=='GET':
        print(request.GET.get('search'))
        print('you hit a get method')
        return Response(courses)
    elif request.method=='POST':
        data = request.data
        print('****')
        print(data)
        print('you hit a post method')
        return Response(courses)
    elif request.method=='PUT':
        print('you hit a put method')
        return Response(courses)

@api_view(['GET','POST','PUT','PATCH'])
def person(request):
    if request.method=='GET':
        # objs = person.object.all()
        objs = Person.objects.all()
        serializer = peopleSerializer(objs,many= True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data=request.data
        serializer = peopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='PUT':
        data=request.data
        serializer = peopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='PATCH':
        data=request.data
        obj = Person.objects.get(id=data['id'])
        serializer = peopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
