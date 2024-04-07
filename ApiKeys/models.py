from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class ApiKey(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    key = models.CharField(max_length=100, default=uuid4)