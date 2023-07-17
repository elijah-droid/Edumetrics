from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Message(models.Model):
    time = models.DateTimeField(default=now)
    sender = models.ForeignKey(User, models.CASCADE)
    reciever = models.ForeignKey(User, models.CASCADE, related_name='message_reciever')
    text = models.TextField(max_length=1000)
