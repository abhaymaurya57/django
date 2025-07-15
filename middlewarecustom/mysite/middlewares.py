from django.shortcuts import HttpResponse

class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response


    def __call__(self,request):
        print('call from middleware before view')
        response= HttpResponse("this page is under construction")
        print('call from middleware after view')
        return response
