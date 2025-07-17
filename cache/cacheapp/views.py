from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
# def home(request):
#     mv = cache.get('movie','has_expired')
#     if mv=='has_expired':
#         cache.set('movie','the oneeee',30)
#         mv = cache.get('movie')
#     return render(request,'cource.html',{'fm':mv})


# def home(request):
#     mv=cache.get_or_set('fees',4000,30)
#     return render(request,'cource.html',{'fm':mv})

# def home(request):
#     cache.delete('fees',version=1)
#     return render(request,'cource.html')

 