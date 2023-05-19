from django.db import models

class BroadCast(models.Model):
    Message = models.TextField(max_length=1000)
    Parents = models.ManyToManyField('Parents.Parent')
    Done = models.BooleanField(default=False)