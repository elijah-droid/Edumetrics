from django.db import models

class Examination(models.Model):
    Name = models.CharField(max_length=100)
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Reports = models.ManyToManyField('Reports.Report', blank=True)
    Date = models.DateField(null=True)
    Classes = models.ManyToManyField('Classes.Class', blank=True)
    mark_sheets = models.ManyToManyField('MarkSheets.MarkSheet')
    Papers = models.ManyToManyField('Paper')
    Open_To_Tallying = models.BooleanField(default=True)

    def __str__(self):
        return self.Name


class Paper(models.Model):
    Examination = models.ForeignKey('Examination', models.CASCADE)
    Subject = models.ForeignKey('Subjects.Subject', models.CASCADE)
    Class = models.ForeignKey('Classes.Class', models.SET_NULL, null=True)
    Date = models.DateTimeField(null=True)
    Time = models.TimeField(null=True)
    Duration = models.CharField(max_length=10)
    Examiner = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True)
    Denominator = models.PositiveIntegerField(default=100)

