from .models import Review, Book
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class BookForm(forms.ModelForm):
    """ A form to create a Book"""
    class Meta:
        model = Book
        fields = (
            'book_title',
            'writer',
            'featured_image',
            'review',
        )
        widgets = {
            'review': SummernoteWidget()
        }