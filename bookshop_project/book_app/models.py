from django.db import models


class Book(models.Model):

    PROSE = 'Prose'
    POETRY = 'Poetry'

    BOOK_TYPES_CHOICES = (
        (PROSE, 'Проза'),
        (POETRY, 'Поэзия')
    )

    title = models.CharField(max_length=70)
    year = models.IntegerField(null=True)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)
    slug = models.SlugField(default="", null=False, db_index=True)
    book_type = models.CharField(null=True, max_length=6, choices=BOOK_TYPES_CHOICES)

    def __str__(self) -> str:
        return str(self.__dict__)
