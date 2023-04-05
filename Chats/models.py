from django.db import models

class Chat(models.Model):
    Users = models.ManyToManyField(User, blank=True)
    Messages = models.ManyToManyField('Messages.Message', blank=True)


class Message(models.Model):
    Sender = models.ForeignKey(User, models.CASCADE, related_name='')
    Reciever = models.ForeignKey(User, models.CASCADE, related_name='')
    Message = models.TextField()