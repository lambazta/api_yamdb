from email.policy import default
from enum import unique
from typing_extensions import Required
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
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
    role = models.TextField(
        'Роль',
        default='user',
    )
