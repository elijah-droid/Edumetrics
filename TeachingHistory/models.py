from django.db import models
from django.utils.timezone import now

class TeachingHistory(models.Model):
    Teacher = models.ForeignKey('Teachers.Teacher', models.CASCADE)
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Subjects = models.ManyToManyField('Subjects.Subject', blank=True)
    Classes = models.ManyToManyField('Classes.Class', blank=True)
    From = models.DateTimeField(null=True)
    To = models.DateTimeField(default=now)
    
