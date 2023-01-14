from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Book
from .forms import ReviewForm, BookForm


class BookList(ListView):
    model = Book
    queryset = Book.objects.order_by("-created_on")
    template_name = "books.html"
    paginate_by = 6


class BookDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.reviews.order_by("-created_on")
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "books_detail.html",
            {
                "book": book,
                "reviews": reviews,
                "liked": liked,
                "review_form": ReviewForm()
            }
        
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Book.objects
        book = get_object_or_404(queryset, slug=slug)
        reviews = book.reviews.order_by("-created_on")
        liked = False
        if book.likes.filter(id=self.request.user.id).exists():
            liked = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.book = book
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "books_detail.html",
            {
                "book": book,
                "reviews": reviews,
                "reviewed": True,
                "liked": liked,
                "review_form": ReviewForm()
            }
        
        )


class BookLike(CreateView):
    """ A view to like a book """

    def post(self, request, slug):
        """ A function to add or remove a like """
        book = get_object_or_404(Book, slug=slug)

        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
        else:
            book.likes.add(request.user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class BookCreate(CreateView):
    """ A view to create a book """

    form_class = BookForm
    template_name = 'create_book.html'
    success_url = "/books/books/"
    model = Book

    def form_valid(self, form):
        """ If form is valid return to Add a book """
        form.instance.author = self.request.user
        messages.success(self.request, 'Book posted successfully')
        return super(BookCreate, self).form_valid(form)


class BookDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete a book """
    model = Book
    template_name = 'book_delete.html'
    success_url = "/books/books/"

    def test_func(self):
        return self.request.user == self.get_object().author
