from django.db import models

class Event(models.Model):
    school =  models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    Classes = models.ManyToManyField('Classes.Class', blank=True)

    def __str__(self):
        return self.title
