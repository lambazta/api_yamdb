from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import UsernameRegexValidator, me_username


class User(AbstractUser):
    ROLES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    ]

    username = models.CharField(
        'Имя пользователя',
        unique=True,
        blank=False,
        max_length=150,
        validators=[UsernameRegexValidator, me_username]
    )
    email = models.EmailField(
        'Почта',
        unique=True,
        blank=False,
    )
    first_name = models.TextField(
        'Имя',
        blank=True,
    )
    last_name = models.TextField(
        'Фамилия',
        blank=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.TextField(
        'Роль',
        choices=ROLES,
        default='user',
    )
    confirmation_code = models.TextField(
        'Код подтверждения',
    )

    class Meta:
        ordering = ('username',)

    def __str__(self):
        return self.username
