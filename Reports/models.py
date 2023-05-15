from django.db import models

class Report(models.Model):
    Student = models.ForeignKey('Students.Student', models.CASCADE)
    Examination = models.ForeignKey('Examinations.Examination', models.CASCADE)
    Results = models.ManyToManyField('Examinations.Result', blank=True)
    Total_Score = models.PositiveIntegerField(null=True)
    Aggregate = models.PositiveIntegerField(null=True)
    Published = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Student) + ' '+str(self.Examination)


class Score(models.Model):
    Report = models.ForeignKey('Report', models.CASCADE)
    Subject = models.ForeignKey('Subjects.Subject', models.CASCADE)
    Score = models.PositiveIntegerField()
    Grade = models.ForeignKey('Grading.Grade', models.SET_NULL, null=True)
    

    def __str__(self):
        return f'{self.Report.Student} - {self.Score} in {self.Subject}'
    