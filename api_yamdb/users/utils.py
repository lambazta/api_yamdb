import random

from django.conf import settings.EMAIL_HOST_USER
from django.core.mail import send_mail

from .models import User


def send_confirmation_code(username, email):
    subject = 'Your account confirmation code'
    confirmation_code = User.code_gen
    message = f'Your confirmation code is {confirmation_code} '
    send_mail(subject, message, EMAIL_HOST_USER, [email])
    user_obj = User.objects.get(username=username)
    user_obj.confirmation_code = confirmation_code
    user_obj.save()
