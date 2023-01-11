from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='books_detail'),
    ]