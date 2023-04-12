from django.shortcuts import render
from . import models
from django.db.models import Count, Model
from django.urls import reverse
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http.request import HttpRequest
from typing import Type


def show_items_from_model(request: HttpRequest, *, the_model: Type[Model], html_path: str) -> HttpResponse:

    items = the_model.objects.all()

    context_data = {
        'items': items
    }

    return render(request, template_name=html_path, context=context_data)


def get_item_by_id(request: HttpRequest, *, the_model: Type[Model], item_id: int, url_alias: str) -> HttpResponseRedirect:

    item = the_model.objects.get(id=item_id)

    return HttpResponseRedirect(reverse(url_alias, args=(item.slug,)))


def get_item_by_slug(request: HttpRequest, *, the_model: Type[Model], item_slug: str, html_path: str) -> HttpResponse:

    item = the_model.objects.get(slug=item_slug)

    context_data = {
        'item': item
    }

    return render(request, html_path, context=context_data)


def get_character_by_id(request: HttpRequest, id: int) -> HttpResponseRedirect:

    return get_item_by_id(request=request, the_model=models.Character, item_id=id, url_alias='character_by_slug')


def get_character_by_slug(request: HttpRequest, character_slug: str) -> HttpResponse:

    return get_item_by_slug(request=request, the_model=models.Character, item_slug=character_slug, html_path='book_app/character.html')


def get_characters(request: HttpRequest) -> HttpResponse:

    return show_items_from_model(request, the_model=models.Character, html_path='book_app/characters.html')


def get_author_by_slug(request, author_slug):

    return get_item_by_slug(request=request, the_model=models.BookAuthor, item_slug=author_slug, html_path='book_app/author.html')


def get_author_by_id(request: HttpRequest, id: int) -> HttpResponseRedirect:

    return get_item_by_id(request=request, the_model=models.BookAuthor, item_id=id, url_alias='author_by_slug')


def get_authors(request):

    return show_items_from_model(request, the_model=models.BookAuthor, html_path='book_app/authors.html')



def get_book_by_slug(request, book_slug):

    return get_item_by_slug(request=request, the_model=models.Book, item_slug=book_slug, html_path='book_app/book.html')


def get_book_by_id(request: HttpRequest, id: int) -> HttpResponseRedirect:

    return get_item_by_id(request=request, the_model=models.Book, item_id=id, url_alias='book_by_slug')


def get_books_mainpage(request):

    books = models.Book.objects.all()

    books_count = books.aggregate(Count('id'))

    context_data = {
        "books": books,
        "books_count": books_count
    }

    return render(request, 'book_app/books.html', context=context_data)
