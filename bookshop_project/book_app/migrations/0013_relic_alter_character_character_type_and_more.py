# Generated by Django 4.1.7 on 2023-04-12 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0012_bookauthor_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='character_type',
            field=models.CharField(choices=[('main', 'Главный персонаж'), ('minor', 'Втоb oростепенный персонаж')], max_length=5),
        ),
        migrations.AddField(
            model_name='character',
            name='character_relic',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_app.relic'),
        ),
    ]
