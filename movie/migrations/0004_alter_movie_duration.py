# Generated by Django 5.0.6 on 2024-05-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=200, verbose_name='Продолжительность'),
        ),
    ]