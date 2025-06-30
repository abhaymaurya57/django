from django.urls import path
from .  import views
from .views import StudentData
urlpatterns = [
    path('book/new/', views.book_create, name='book-create'),
    path('', views.book_list, name='book-list'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('book/<int:pk>/edit/', views.book_update, name='book-update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book-delete'),
    path('student/', StudentData.as_view(), name='student'),
     path('student/<int:id>/', StudentData.as_view(), name='student'),

]

