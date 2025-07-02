from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentModelViewSet

router = DefaultRouter()
router.register(r'student', StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
