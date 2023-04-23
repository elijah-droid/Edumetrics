from django.db import models
from django.contrib.auth.models import User

sectors = (
    ('Book Shop', 'Book Shop'),
    ('Scholastics', 'Scholastics'),
    ('School Supply', 'School Supply')
)


class Product(models.Model):
    Name = models.CharField(max_length=100)
    Sector = models.CharField(max_length=20, choices=sectors)
    Price = models.PositiveIntegerField()


class Cart(models.Model):
    Buyer = models.OneToOneField(User, models.CASCADE)
    Products = models.ManyToManyField('Product')
