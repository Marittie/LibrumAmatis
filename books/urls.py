from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='books_detail'),
    path('like/<slug:slug>', views.BookLike.as_view(), name='book_like'),
    ]