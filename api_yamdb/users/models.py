from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = [
        ('User', 'User'),
        ('Moderator', 'Moderator'),
        ('Admin', 'Admin'),
    ]

    username = models.CharField(
        'Имя пользователя',
        unique=True,
        blank=False,
        max_length=150,
    )
    email = models.EmailField(
        'Почта',
        blank=False,
    )
    first_name = models.TextField(
        'Имя',
    )
    last_name = models.TextField(
        'Фамилия',
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        choices=ROLES,
        default='User',
        max_length=50
    )
