from django.shortcuts import render,HttpResponse
from .models import Watchlist,StremPlatform
from .serializers import WatchListSerializer,stremPlatformserializer
from django.http import JsonResponse
# Create your views here.
def movie_list(request):
    movie_list  = Watchlist.objects.all()
    serialized = WatchListSerializer(movie_list,many = True)
    return HttpResponse(serialized.data)

def movie_detail(request,pk):
    movie = Watchlist.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return JsonResponse(serialized.data,save=False)
