import random

from django.core.mail import send_mail

from .models import User


def send_confirmation_code(username, email):
    subject = 'Your account confirmation code'
    confirmation_code = random.randint(100000, 999999)
    message = f'Your confirmation code is {confirmation_code} '
    send_mail(subject, message, 'from@example.com', [email])
    user_obj = User.objects.get(username=username)
    user_obj.confirmation_code = confirmation_code
    user_obj.save()
