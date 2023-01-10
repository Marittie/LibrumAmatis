from django.shortcuts import render
from django.views import generic, View
from .models import Book


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(status=1).order_by("-created_on")
    template_name = "books.html"
    paginate_by = 6


