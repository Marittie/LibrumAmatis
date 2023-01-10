from django.contrib import admin
from .models import Book, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    """ A class to display books posts to admin """
    list_display = ('book_title', 'updated_on')
    search_fields = ['book_title', 'content']
    list_filter = ('updated_on',)
    summernote_fields = ('content')
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'book', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'email', 'body')
