from django.shortcuts import render
from django.http import HttpResponse

#import models
from .models import Book, Author, BookInstance, Genre, Language

# Create your views here.

def index(request):
    """ View for index page """

    #Generate counts of main model objects

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available book instances

    num_available_instances = BookInstance.objects.filter(status__exact='a').count()

    #'all( )' is implied   ?
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_available_instances,
        'num_authors' : num_authors,
        'author' : 'mustafa',
    }
    return render(request, 'index.html', context)

