from django.shortcuts import render

# Create your views here.
def hii(request):
    return render(request,"hii.html")