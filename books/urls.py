from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.BookList.as_view(), name='books'),
    path('create/', views.BookCreate.as_view(), name='create_book'),
    path('delete/<slug:slug>', views.BookDelete.as_view(), name='book_delete'),
    path('edit/<slug:slug>', views.BookEdit.as_view(), name='book_edit'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='books_detail'),
    path('like/<slug:slug>', views.BookLike.as_view(), name='book_like'),
    
    ]