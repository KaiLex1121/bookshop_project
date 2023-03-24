from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'rating', 'status_by_rating', 'book_type')
    ordering = ('-title', 'rating')

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


admin.site.register(Book, BookAdmin)
