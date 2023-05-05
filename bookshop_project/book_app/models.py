from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class UploadedFiles(models.Model):
    uploaded_file = models.FileField(verbose_name='Файл', upload_to='uploaded_files')

class FeedBackModel(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    description = models.TextField()
    rating = models.IntegerField(validators=(MaxValueValidator(5),))

    def __str__(self) -> str:
        return f'Комментарий № {self.id}'


class Relic(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400, null=True, blank=True)
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self) -> str:
        return self.name


class Character(models.Model):

    MAIN = 'main'
    MINOR = 'minor'

    CHARACTER_TYPE_CHOICES = (
        (MAIN, 'Главный персонаж'),
        (MINOR, 'Втоb oростепенный персонаж')
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    character_type = models.CharField(max_length=5, choices=CHARACTER_TYPE_CHOICES)
    character_relic = models.OneToOneField(Relic, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self) -> str:
        return self.name


class BookAuthor(models.Model):

    M = 'M'
    F = 'F'

    GENDER_CHOICES = (
        (M, 'Мужчина'),
        (F, 'Женщина')
    )

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, default=M, choices=GENDER_CHOICES)
    slug = models.SlugField(null=False, db_index=True)

    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'


class Book(models.Model):

    PROSE = 'Prose'
    POETRY = 'Poetry'

    BOOK_TYPES_CHOICES = (
        (PROSE, 'Проза'),
        (POETRY, 'Поэзия')
    )

    title = models.CharField(max_length=70)
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    rating = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    is_best_selling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    book_type = models.CharField(null=True, max_length=6, choices=BOOK_TYPES_CHOICES, blank=True)
    author = models.ForeignKey(BookAuthor, on_delete=models.PROTECT, null=True)
    characters = models.ManyToManyField(Character)

    def __str__(self) -> str:
        return str(self.title)
