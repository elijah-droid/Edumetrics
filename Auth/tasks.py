from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task
def send_lesson_reminders():
    print('hello world')