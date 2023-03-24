from django.db import models

class Tally(models.Model):
    User = models.ForeignKey()
    Score = models.ForeignKey('Reports.Score', )
    From = models.PositiveIntegerField(null=True)
    To = models.PositiveIntegerField(null=True)
