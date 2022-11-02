from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User
from app.models import Titles


class Reviews(models.Model):
    title_id = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Название произведения'
    )
    text = models.TextField(
        verbose_name='Ваш отзыв',
        help_text='Введите текст вашего отзыва'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор отзыва'
    )
    score = models.IntegerField(
        default=1,
        max_digits=2,
        blank=True,
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name


class Comments(models.Model):
    review_id = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(
        verbose_name='Комментарий',
        help_text='Текст комментария'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]
from django.db import models

from .validators import validate_year


class Category(models.Model):
    name = models.CharField(
        'Название',
        max_length=100
    )
    slug = models.SlugField(
        'Идентификатор',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name[:30]


class Genre(models.Model):
    name = models.CharField(
        'Название',
        max_length=100
    )
    slug = models.SlugField(
        'Идентификатор',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name[:30]


class Title(models.Model):
    name = models.CharField(
        'Название',
        max_length=200
    )
    year = models.IntegerField(
        'Год выпуска',
        validators=[validate_year]
    )
    description = models.TextField(
        'Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )
    rating = models.IntegerField(
        'Рейтинг',
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']

    def __str__(self):
        return self.name[:30]
