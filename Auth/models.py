from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class PasswordReset(models.Model):
    User = models.ForeignKey(User, models.CASCADE)
    Date = models.DateTimeField(default=now)
    current_otp = models.CharField(max_length=100)
    