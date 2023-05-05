from django.shortcuts import render
from django.db.models import Count, Model
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from django.http.request import HttpRequest
from django.views.generic import ListView, TemplateView, DetailView, FormView, UpdateView, View
from . import models, forms
from typing import Type

class SuccesfulUpload(TemplateView):
    template_name = 'book_app/successful_file_upload.html'


class LoadFile(View):

    def get_template_path(self):
        return 'book_app/upload_file_form.html'

    def get(self, request):
        form = forms.LoadFileForm()
        return render(request, self.get_template_path(), context={'form': form})

    def post(self, request):
        form = forms.LoadFileForm(request.POST, request.FILES)
        file = request.FILES['uploaded_file']

        if form.is_valid():
            models.UploadedFiles.objects.create(uploaded_file=file)
            return HttpResponseRedirect(reverse_lazy('upload_successful'))

        return render(request, self.get_template_path(), context={'form': form})


class DetailFeedback(DetailView):
    template_name = 'book_app/detail_feedback.html'
    model = models.FeedBackModel
    context_object_name = 'feedback'


class ListFeedback(ListView):
    template_name = 'book_app/feedback_list.html'
    model = models.FeedBackModel
    context_object_name = 'feedbacks'


class SuccessfulFeedback(TemplateView):
    template_name = 'book_app/successful_feedback.html'


class CreateView(FormView):
    template_name = 'book_app/feedback_form.html'
    form_class = forms.FeedBackForm
    success_url = reverse_lazy('feedback_success')

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class EditFeedback(UpdateView):
    form_class = forms.FeedBackForm
    model = models.FeedBackModel
    success_url = reverse_lazy('feedback_success')
    template_name = 'book_app/feedback_form.html'


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
