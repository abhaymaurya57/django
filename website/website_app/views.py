from django.shortcuts import render

from django.contrib.auth import views as auth_views


# Create your views here.
def hii(request):
    return render(request,"hii.html")

