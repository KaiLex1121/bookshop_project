from django.contrib import admin
from .models import Book, BookAuthor, Character, Relic, FeedBackModel, UploadedFiles
from django.db.models import QuerySet
from django.utils.text import slugify
from django.http import HttpRequest
from typing import Any, Optional, List, Tuple

@admin.register(UploadedFiles)
class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = ('uploaded_file',)


@admin.register(FeedBackModel)
class FeedBackModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'description', 'rating')


@admin.register(Relic)
class RelicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'character')
    prepopulated_fields = {
        "slug": ('name',)
    }


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'character_type', 'character_relic')
    list_editable = ('description', 'character_type', 'character_relic')
    prepopulated_fields = {
        "slug": ('name',)
    }


@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'slug')
    prepopulated_fields = {
        "slug": ('name', 'last_name')
    }


class RatingFilter(admin.SimpleListFilter):

    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request: Any, model_admin: Any) -> List[Tuple[Any, str]]:
        return [
            ('0-49', 'Хуже среднего'),
            ('50-100', 'Лучше среднего')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> Optional[QuerySet[Any]]:
        if self.value():
            rating = self.value().split('-')
            lowest_rating, highest_rating = rating[0], rating[1]
            return queryset.filter(rating__gte=lowest_rating).filter(rating__lte=highest_rating)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'rating', 'author')
    ordering = ('-title', 'rating')
    actions = ('set_slug',)
    search_fields = ('title',)
    list_editable = ('rating', 'author')
    list_filter = [RatingFilter]
    filter_horizontal = ('characters',)
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
