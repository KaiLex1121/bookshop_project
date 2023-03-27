from django.contrib import admin
from .models import Book
from django.db.models import QuerySet
from django.utils.text import slugify
from django.http import HttpRequest


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'rating', 'status_by_rating', 'book_type')
    ordering = ('-title', 'rating')
    actions = ('set_slug',)
    search_fields = ('title',)
    prepopulated_fields = {
        "slug": ('title',)
    }

    @admin.display(description='Book Status')
    def status_by_rating(self, book: Book) -> str:
        if book.rating < 50:
            return 'Shit'
        if book.rating < 75:
            return 'So-so'
        return 'Good'

    @admin.action(description='Проставить слаг на основании имени')
    def set_slug(self, request: HttpRequest, query_set: QuerySet) -> None:

        for obj in query_set:
            obj.slug = slugify(obj.title)
            obj.save()

        self.message_user(
            request,
            message=f'Было обновлено {query_set.count()} записей'
        )


admin.site.register(Book, BookAdmin)
