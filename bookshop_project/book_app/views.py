from django.shortcuts import render
from . import models
from django.db.models import Count

def get_books_mainpage(request):

    books = models.Book.objects.all()

    books_count = books.aggregate(Count('id'))

    context_data = {
        "books": books,
        "books_count": books_count
    }

    return render(request, 'book_app/base.html', context=context_data)
