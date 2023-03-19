from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Attendance(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Date = models.DateField(default=now)
    Students = models.PositiveIntegerField(default=0)
    Teacher = models.PositiveIntegerField(default=0)
