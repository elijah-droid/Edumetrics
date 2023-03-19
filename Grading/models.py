from django.db import models

grades =  (
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('C3', 'C3'),
    ('C4', 'C4'),
    ('C5', 'C5'),
    ('C6', 'C6'),
    ('P7', 'P7'),
    ('P8', 'P8'),
    ('F9', 'F9'),
    ('A', 'A'),
    ('B', 'B'),
    ('Ungraded', 'Ungraded')
)

divisions = (
    ('First Grade', 'First Grade'),
    ('Second Grade', 'Second Grade'),
    ('Third Grade', 'Third Grade'),
    ('Fourth Grade', 'Fourth Grade')
)

class Grade(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Name = models.CharField(max_length=100, choices=grades)
    From = models.PositiveIntegerField(null=True)
    To = models.PositiveIntegerField(null=True)
    Value = models.PositiveIntegerField(null=True)
    Classes = models.ManyToManyField('Classes.Class')


class Division(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Name = models.CharField(max_length=100, choices=divisions)
    From = models.PositiveIntegerField(null=True)
    To = models.PositiveIntegerField(null=True)
    Classes = models.ManyToManyField('Classes.Class')