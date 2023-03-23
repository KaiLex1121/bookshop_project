from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'rating')
    prepopulated_fields = {
        "slug": ('title',)
    }


admin.site.register(Book, BookAdmin)
