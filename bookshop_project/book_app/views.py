from django.shortcuts import render
from . import models
from django.db.models import Count
from django.urls import reverse
from django.http.response import HttpResponseRedirect


def get_author_by_slug(request, book_slug):

    author = models.BookAuthor.objects.get(slug=book_slug)

    context_data = {
        "author": author
    }

    return render(request, 'book_app/author.html', context=context_data)


def get_author_by_id(request, id):

    author = models.BookAuthor.objects.get(id=id)

    return HttpResponseRedirect(reverse('author_by_slug', args=(author.slug,)))


def get_authors(request):

    authors = models.BookAuthor.objects.all()

    context_data = {
        "authors": authors,
    }

    return render(request, 'book_app/authors.html', context=context_data)


def get_books_mainpage(request):

    books = models.Book.objects.all()

    books_count = books.aggregate(Count('id'))

    context_data = {
        "books": books,
        "books_count": books_count
    }

    return render(request, 'book_app/base.html', context=context_data)
