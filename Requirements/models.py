from django.db import models

class Requirement(models.Model):
    Name = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=50, null=True)
    Programme = models.ForeignKey('Programmes.Programme', models.CASCADE)