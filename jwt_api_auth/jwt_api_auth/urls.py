
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jwt_token.urls')),
    path("",include("api.urls")),


    path("__reload__/", include("django_browser_reload.urls")),
]
