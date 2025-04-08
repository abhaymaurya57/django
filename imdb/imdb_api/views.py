from django.shortcuts import render,HttpResponse
from django.http import Http404
from django.http import JsonResponse


from .models import Watchlist,StremPlatform
from .serializers import WatchListSerializer,streamPlatformserializer


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# **********entry point************
from rest_framework.reverse import reverse
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('movie-list', request=request, format=format),
        'streamlist': reverse('stream-platform', request=request, format=format)
    })

# *********Rewriting our API using class-based views******


# class StreamPlatformList(APIView):
#     def get(self, request, format=None):
#         stream_list = StremPlatform.objects.all()
#         serialized = streamPlatformserializer(stream_list, many=True)
#         return Response(serialized.data)

#     def post(self,request,format=None):
#         serialized = streamPlatformserializer(data = request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status=status.HTTP_201_CREATED)
#         return Response(serialized.errors ,status=status.HTTP_400_BAD_REQUEST)


# class StreamPlatformDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return StremPlatform.objects.get(pk=pk)
#         except StremPlatform.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         serializer = streamPlatformserializer(obj)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         serializer = streamPlatformserializer(obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         obj = self.get_object(pk)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
# Create your views here.
def movie_list(request):
    movie_list  = Watchlist.objects.all()
    serialized = WatchListSerializer(movie_list,many = True)
    return Response(serialized.data)


@api_view(['GET'])
def movie_detail(request,pk):
    movie = Watchlist.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return Response(serialized.data)

# @api_view(['GET','POST'])
# def stream_list(request,format=None):
#     if request.method == 'GET':
#         stream_list  = StremPlatform.objects.all()
#         serialized = streamPlatformserializer(stream_list,many = True)
#         return Response(serialized.data)
    
#     elif request.method =='POST':
#         _data = request.data
#         serialized = streamPlatformserializer(data = _data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status=status.HTTP_201_CREATED)
#         return Response(serialized.errors ,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','DELETE','PUT'])
# def stream_detail(request,pk,format=None):
#     # StreamPlatform = StreamPlatform.objects.get(pk=pk)
#     stream_platform = StremPlatform.objects.get(pk=pk)
#     serialized = streamPlatformserializer(stream_platform)
#     return Response(serialized.data)



# Using mixins

from rest_framework import mixins
from rest_framework import generics

# class StreamPlatformList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = StremPlatform.objects.all()
#     serializer_class = streamPlatformserializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class StreamPlatformDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = StremPlatform.objects.all()
#     serializer_class = streamPlatformserializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# *******************Using generic class-based views**********************


from rest_framework import generics


# class StreamPlatformList(generics.ListCreateAPIView):
#     queryset = StremPlatform.objects.all()
#     serializer_class = streamPlatformserializer


# class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StremPlatform.objects.all()
#     serializer_class = streamPlatformserializer

from rest_framework import viewsets
class StreamPlatformViewSet(viewsets.ModelViewSet):
    queryset = StremPlatform.objects.all()
    serializer_class = streamPlatformserializer