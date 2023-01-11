from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView)
from .models import Book


class BookList(ListView):
    model = Book
    queryset = Book.objects.filter(status=1).order_by("-created_on")
    template_name = "books.html"
    paginate_by = 6


class BookDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(status=1)
        book = get_object_or_404(queryset, slug=slug)
        comments = book.reviews.order_by("-created_on")
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "books_detail.html",
            {
                "book": book,
               
            }
        
        )
