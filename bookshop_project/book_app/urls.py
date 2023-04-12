from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.get_books_mainpage),
    path('books/<int:id>/', views.get_book_by_id, name='book_by_id'),
    path('books/<slug:book_slug>/', views.get_book_by_slug, name='book_by_slug'),
    path('authors/', views.get_authors),
    path('authors/<int:id>/', views.get_author_by_id, name='author_by_id'),
    path('authors/<slug:author_slug>/', views.get_author_by_slug, name='author_by_slug'),
    path('characters/', views.get_characters),
    path('characters/<int:id>/', views.get_character_by_id, name='character_by_id'),
    path('characters/<slug:character_slug>/', views.get_character_by_slug, name='character_by_slug'),
]
