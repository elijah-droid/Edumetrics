from django.db import models
from django.utils.timezone import now

class Book(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Name = models.CharField(max_length=100)
    Number = models.PositiveBigIntegerField(default=0)
    For_Classes = models.ManyToManyField('Classes.Class')
    Lend_Outs  = models.ManyToManyField('LendOut', blank=True)


class LendOut(models.Model):
    Book = models.ForeignKey('Book', models.CASCADE)
    Student = models.ForeignKey('Students.Student', models.CASCADE)
    Date = models.DateTimeField(default=now)
    Number = models.PositiveIntegerField(default=1)
    Returned = models.BooleanField(default=False)