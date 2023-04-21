from django.db import models
from django.contrib.auth.models import User

class Tally(models.Model):
    Mark_Sheet = models.ForeignKey('MarkSheets.MarkSheet', models.SET_NULL, null=True)
    Teacher = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True)
    Student = models.ForeignKey('Students.Student', models.SET_NULL, null=True)
    Score = models.PositiveIntegerField(null=True)
    Grade = models.ForeignKey('Grading.Grade', models.SET_NULL, null=True, blank=True)


                                                                                                                                                                                                       