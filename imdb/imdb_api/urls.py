from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
streamplatform_list = views.StreamPlatformViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
streamplatform_detail = views.StreamPlatformViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    
    path('list/',views.movie_list,name='watchlist-list'),
    path('list/<int:pk>',views.movie_detail,name='watchlist-detail'),
    path('stream/',views.StreamPlatformList.as_views(),name = 'streamplatform-list'),
    path('stream/<int:pk>',views.StreamPlatformDetail.as_views(),name = 'streamplatform-detail'),
    path('', views.api_root),
]
 
urlpatterns = format_suffix_patterns(urlpatterns)