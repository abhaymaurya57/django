from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('teachers',views.TeacherViewset)
router.register('subjects',views.subjectviewset)
urlpatterns = [
    path('',include(router.urls)),
]
