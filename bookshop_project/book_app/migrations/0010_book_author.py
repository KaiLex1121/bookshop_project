# Generated by Django 4.1.7 on 2023-03-30 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0009_alter_bookauthor_last_name_alter_bookauthor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book_app.bookauthor'),
        ),
    ]
