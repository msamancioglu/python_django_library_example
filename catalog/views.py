from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import os
#import models
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """" generic class based list view for books borrowed by current user """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact = 'o').order_by('due_back')

        #return BookInstance.objects.get(pk=1)


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
    #paginate_by = 10


class AuthorListView(LoginRequiredMixin,generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author
    #paginate_by = 10

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.

@login_required
def index(request):
    """ View for index page """

    #Generate counts of main model objects

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available book instances

    num_available_instances = BookInstance.objects.filter(status__exact='a').count()

    #'all( )' is implied   ?
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'pat':os.path.join(BASE_DIR, 'templates'),
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_available_instances,
        'num_authors' : num_authors,
        'author' : 'mustafa',
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context)

@login_required
def hello(request):
    return HttpResponse('Helo')