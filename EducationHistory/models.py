from django.db import models
from django.utils.timezone  import now

class EducationHistory(models.Model):
    Student = models.ForeignKey('Students.Student', models.CASCADE)
    School = models.ForeignKey('Schools.School', models.CASCADE)
    From = models.DateTimeField(null=True)
    To = models.DateTimeField(default=now)
