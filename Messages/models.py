from django.db import models
from django.contrib.auth.models import User

class Messages(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    message = models.TextField(max_length=1000)
    
