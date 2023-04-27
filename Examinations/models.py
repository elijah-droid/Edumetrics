from django.db import models

class Examination(models.Model):
    Name = models.CharField(max_length=100)
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Reports = models.ManyToManyField('Reports.Report', blank=True)
    Date = models.DateField(null=True)
    Classes = models.ManyToManyField('Classes.Class', blank=True)
    mark_sheets = models.ManyToManyField('MarkSheets.MarkSheet')
    Open_To_Tallying = models.BooleanField(default=True)

    def __str__(self):
        return self.Name