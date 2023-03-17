from django.shortcuts import render
from . import models


def get_books_mainpage(request):

    books = models.Book.objects.all()

    context_data = {
        "books": books
    }

    return render(request, 'book_app/base.html', context=context_data)
