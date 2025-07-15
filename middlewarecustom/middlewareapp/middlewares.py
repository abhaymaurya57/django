#get_response agar last middleware hai to yahi chlega nahi to views hai to views chalega
def my_middleware(get_response):
    print("one time initialization")

    def my_function(request):
        print("this is before view")

        response=get_response(request)
        print("this is after view")
      
        return response
    return my_function