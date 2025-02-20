from django.http import HttpResponse
from django.shortcuts import render

def chek(request):
    # return HttpResponse("hello,world you are at home page")
    return render(request,'chek.html')