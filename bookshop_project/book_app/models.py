from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=70)
    year = models.IntegerField(null=True)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.__dict__)