# Generated by Django 4.1.7 on 2023-03-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]