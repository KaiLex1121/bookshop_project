# Generated by Django 4.1.7 on 2023-03-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0008_bookauthor_remove_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
