from django.conf import settings.MIN_VALUE, settings.MAX_VALUE
from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import UsernameRegexValidator, me_username


class User(AbstractUser):
    USER = 'USR'
    MODERATOR = 'MDR'
    ADMIN = 'ADM'
    ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
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
        max_length=3,
        choices=ROLE_CHOICES,
        default=USER,
    )
    confirmation_code = models.TextField(
        'Код подтверждения',
    )

    class Meta:
        ordering = ('username',)

    @property
    def is_admin(self):
        self.role == ADMIN
         
    @property
    def is_moderator(self):
        self.role == MODERATOR

    @property
    def code_gen(self):
        random_int=random.randint(MIN_VALUE, MAX_VALUE)
        return random_int
        

    def __str__(self):
        return self.username
