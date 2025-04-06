from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import peopleSerializer
# Create your views here.
# person.object.all()
# [1,2,3,4] -> queryset



@api_view(['GET','POST','put','patch'])
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

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = peopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = peopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        try:
            obj = Person.objects.get(id=request.data['id'])
            serializer = peopleSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

    elif request.method == 'PATCH':
        try:
            obj = Person.objects.get(id=request.data['id'])
            serializer = peopleSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)

    elif request.method == 'DELETE':
        try:
            obj = Person.objects.get(id=request.data['id'])
            obj.delete()
            return Response({'message': 'Person deleted'})
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
