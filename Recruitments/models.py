from django.db import models

class ClassRecruitment(models.Model):
    Teacher = models.ForeignKey('Teachers.Teacher', models.CASCADE)
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Class = models.ManyToManyField('Classes.Class')
    Subjects = models.ManyToManyField('Subjects.Subject')

    def __str__(self):
        return f'{self.Teacher.__str__().upper()} @ {self.School}'
