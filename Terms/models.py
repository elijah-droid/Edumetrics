from django.db import models

terms = (
    ('Term One', 'Term One'),
    ('Term Two', 'Term Two'),
    ('Term Three', 'Term Three')
)

class Term(models.Model):
    Name = models.CharField(max_length=10, choices=terms)
    School = models.ForeignKey('Schools.School', models.CASCADE)
    From = models.DateField()
    To = models.DateField()