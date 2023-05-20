from django.db import models

class TelConfirmation(models.Model):
    Contact = models.PositiveIntegerField()
    Code = models.CharField(max_length=10)



