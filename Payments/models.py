from django.db import models

class Payment(models.Model):
    txid = models.CharField(max_length=100)
    amount = models.IntegerField(null=True)
    wallet = models.CharField(max_length=20)
    account = models.PositiveIntegerField(null=True)
    Status = models.CharField(max_length=20)