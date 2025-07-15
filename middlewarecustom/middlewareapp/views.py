from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

#functionbase
def home(request):
    print("i am view")
    return HttpResponse("this is home page") 


def excp(request):
    print("i excp view")
    a=10/0
    return HttpResponse("this is excp page") 

def user_info(request):
    print("i am User Info view")
    context={'name':"abhay"}
    return TemplateResponse(request,'user.html',context)
