from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Book(models.Model):
    """A model to create Book items"""
    book_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=False, unique=True)
    writer = models.CharField(max_length=200, unique=True,)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_books"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='books_like', blank=True)

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse("books_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.book_title)
        return super().save(*args, **kwargs)

    class Meta:
        """Created on order"""
        ordering = ["-created_on"]

    def __str__(self):
        return self.book_title

    def number_of_likes(self):
        """Books likes"""
        return self.likes.count()


class Review(models.Model):
    """ A model to make a review """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Order by created on date """
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"
