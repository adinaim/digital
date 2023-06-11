from django.conf import settings
# from config.celery import app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model
# from celery import shared_task

User = get_user_model()

# @app.task
# def send_activation_sms(phone, activation_code):
#     from twilio.rest import Client
#     client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH_TOKEN)
#     message = client.messages.create(
#         body=f'This is your activation code: {activation_code}',
#         from_=settings.TWILIO_NUMBER,
#         to=phone
#     )

# @app.task
def send_activation_code(email, activation_code):
    activation_link = f'http://localhost:8000/account/activate/{activation_code}/'
    html_message = render_to_string(
        'user/code_mail.html',
        {'activation_link': activation_link}
        )
    send_mail(
        'Активируйте ваш аккаунт!',
        '',
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_message,
        fail_silently=False   
    )

# @shared_task(name='check_activation')
def check_activation():               
    today = datetime.now(timezone.utc)
    for user in User.objects.filter(is_active=False) and ((today - user.created_at).seconds/3600) > 24:
        user.delete()