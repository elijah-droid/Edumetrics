from django.db import models

class Circular(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    Classes = models.ManyToManyField('Classes.Class')

