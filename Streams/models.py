from django.db import models

class Stream(models.Model):
    Name = models.CharField(max_length=100)
    Students = models.ManyToManyField('Students.Student')

    def __str__(self):
        return self.Name