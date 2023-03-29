from django.db import models
from django.contrib.auth.models import User

relationships = (
    ('Mother', 'Mother'),
    ('Father', 'Father'),
    ('Aunt', 'Aunt'),
    ('Uncle', 'Uncle'),
    ('GrandMother', 'GrandMother'),
    ('GrandFather', 'GrandFather')
)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relationships = models.ManyToManyField('Relationship', blank=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Relationship(models.Model):
    Parent = models.ForeignKey('Parents.Parent', models.CASCADE)
    Child = models.ForeignKey('Students.Student', models.CASCADE)
    Relationship = models.CharField(max_length=100, choices=relationships)

    

