from django.db import models

class Stream(models.Model):
    Class = models.ForeignKey('Classes.Class', models.SET_NULL, null=True)
    Name = models.CharField(max_length=100)
    Class_Teacher = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True, blank=True)
    Students = models.ManyToManyField('Students.Student')


    def __str__(self):
        return self.Name