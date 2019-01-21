# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from booklib.models import Genre, Author, Book, BookInstance

def index(request):
    objects = Book()
    books_list = Book.objects.all().order_by('id')
    date_dict = {'all_books': books_list}
    return render(
        request,
        'booklib/index.html',
        context=date_dict
    )

def booklib_index(request):
    return HttpResponse(
        "Booklib index page"
    )

def booklib_statistics(request):
    """
        Total books in lib. Statistical page
    """
    # Generate quantitty values:
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_authors=Author.objects.count()
    num_genres=Genre.objects.count()
    
    return render(
        request,
        'booklib/booklib_statistics.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_authors':num_authors,
            'num_genres':num_genres
        },
    )

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    
class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book