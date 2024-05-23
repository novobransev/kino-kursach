from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    genre = models.CharField(max_length=200, verbose_name='Жанр')
    release_year = models.IntegerField(verbose_name='Год выпуска')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    duration = models.CharField(max_length=200, verbose_name='Продолжительность')
    age_rating = models.CharField(max_length=10, verbose_name='Возрастное ограничение', null=True)
    country = models.CharField(max_length=50, verbose_name='Страна')
    actors = models.ManyToManyField('Actor', related_name='movies', verbose_name='Актеры')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(verbose_name='Рейтинг')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    poster = models.URLField(null=True, blank=True, verbose_name='Постер')
    trailer = models.URLField(null=True, blank=True, verbose_name='Трейлер')

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', verbose_name='Фильм')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True, verbose_name='Аватар')
    purchased_movies = models.ManyToManyField(Movie, related_name='purchased_by', verbose_name='Купленные фильмы',null=True, blank=True)
    favorite_movies = models.ManyToManyField(Movie, related_name='favorited_by', verbose_name='Избранные фильмы',null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    photo = models.URLField(null=True, blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Актерa'
        verbose_name_plural = 'Актеры'

    def __str__(self):
        return self.name
