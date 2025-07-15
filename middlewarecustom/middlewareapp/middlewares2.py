class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time initialization")

    def __call__(self,request):
        print("this is before views")
        response = self.get_response(request)
        print("this is after views")
        return response

class YourMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time your  initialization")

    def __call__(self,request):
        print("this is your  before views")
        response = self.get_response(request)
        print("this is  your after views")
        return response

class SheMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time she  initialization")
        
    def __call__(self,request):
        print("this is she  before views")
        response = self.get_response(request)
        print("this is  she after views")
        return response
