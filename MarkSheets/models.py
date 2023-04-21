from django.db import models

class MarkSheet(models.Model):
    Exam = models.ForeignKey('Examinations.Examination', models.SET_NULL, null=True)
    Class = models.ForeignKey('Classes.Class', models.SET_NULL, null=True)
    Subject = models.ForeignKey('Subjects.Subject', models.SET_NULL, null=True)
    Tallies = models.ManyToManyField('Tallies.Tally', blank=True)
