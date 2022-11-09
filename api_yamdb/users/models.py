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
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=30,
        choices=ROLES,
        default='user',
    )
    confirmation_code = models.TextField(
        'Код подтверждения',
    )

    class Meta:
        ordering = ('username',)

    @property
    def is_admin(self):
        if self.role == 'admin':
            return True
        return False

    @property
    def is_moderator(self):
        if self.role == 'moderator':
            return True
        return False

    def __str__(self):
        return self.username
