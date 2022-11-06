from django.core.mail import send_mail
import random
from .models import User
# from django.contrib.auth.hashers import make_password


def send_confirmation_code(username, email):
    subject = 'Your account confirmation code'
    confirmation_code = random.randint(100000, 999999)
    message = f'Your confirmation code is {confirmation_code} '
    send_mail(subject, message, 'from@example.com', [email])
    # confirmation_code = make_password(confirmation_code)
    user_obj = User.objects.get(username=username)
    user_obj.confirmation_code = confirmation_code
    user_obj.save()
