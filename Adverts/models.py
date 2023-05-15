from django.db import models

class Advert(models.Model):
    School = models.ForeignKey()