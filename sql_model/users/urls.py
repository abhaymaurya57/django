from django.urls import path
# from . import views
from .views import person

urlpatterns = [
    # path('',views.all_user)
    # path('users/', user_list, name='User'),
    path('persons/', person, name='Person'),
]
