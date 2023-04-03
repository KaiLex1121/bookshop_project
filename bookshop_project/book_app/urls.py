from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.get_books_mainpage),
    path('authors/', views.get_authors),
    path('authors/<int:id>/', views.get_author_by_id, name='author_by_id'),
    path('authors/<slug:book_slug>/', views.get_author_by_slug, name='author_by_slug')
]
