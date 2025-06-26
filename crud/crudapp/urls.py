from django.urls import path
from .  import views
from django.urls import path
from . import views

urlpatterns = [
    path('book/new/', views.book_create, name='book-create'),
    path('', views.book_list, name='book-list'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/<int:pk>/edit/', views.book_update, name='book-update'),     # ✅ fix
    path('book/<int:pk>/delete/', views.book_delete, name='book-delete'),   # ✅ fix
]

