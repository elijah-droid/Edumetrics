from django.db import models
from django.contrib.auth.models import User

class Tally(models.Model):
    User = models.ForeignKey(User, models.CASCADE)
    Score = models.ForeignKey('Reports.Score', models.CASCADE)
    From = models.PositiveIntegerField(null=True)
    To = models.PositiveIntegerField(null=True)


                                                                                                                                                                                                       