from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response= self.get_response(request)
        return response
    
    def process_view(request,*arg,**kwargs):
        print("this is print process view -  before view")
        # return HttpResponse("this is before view")
        return None
    
class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response= self.get_response(request)
        return response
    
    def process_exception(self,request,exception):
        print("exeption occured")
        msg=exception
        class_name=exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)
        # return None

   
class MyTemplateMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response= self.get_response(request)
        return response
    
    def process_template_response(self,request,response):
        print("process Template REsponse From Middleware")
        response.context_data['name']='sonam'
        return response