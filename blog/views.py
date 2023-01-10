from django.shortcuts import render
from django.views import generic


def index(request):
    """ Return homepage """
    return render(request, 'index.html')
