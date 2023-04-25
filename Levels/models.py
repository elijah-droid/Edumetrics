from django.db import models


names = (
    ('Nursery', 'Nursery'),
    ('Primary', 'Primary'),
    ('Secondary Ordinary Level', 'Secondary Ordinary'),
    ('Secondary Advanced Level', 'Secondary Advanced'),
    ('Tertiary', 'Tertiary')
)

class Level(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Name = models.CharField(max_length=100, choices=names)
    Subjects = models.ManyToManyField('Subjects.Subject')
    Classes = models.ManyToManyField('Classes.Class')