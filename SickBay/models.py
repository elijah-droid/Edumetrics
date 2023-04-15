from django.db import models
from django.utils.timezone import now

class Admission(models.Model):
    Student = models.ForeignKey('Students.Student', models.CASCADE)
    Time = models.DateTimeField(default=now)
    Complications = models.TextField(max_length=10000)
    Examined_By = models.ForeignKey('SchoolAdministrators.SchoolAdministrator', models.CASCADE)
    Dismissed = models.DateTimeField(null=True)
