from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Person

# Create your views here.
# def all_user(request):
#     return HttpResponse('Returning all User')

from django.http import JsonResponse
# def user_list(request):
#     users = list(User.objects.values('email', 'password'))
#     return JsonResponse({'users': users})

# def person_list(request):  
#     persons = list(Person.objects.values('first_name', 'last_name'))  # Fetch Person model data
#     return JsonResponse({'persons': persons})

def person(request):
    person = Person.objects.all()
    return render(request, 'user.html', {'person': person})