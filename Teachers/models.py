from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    work_profile = models.ManyToManyField('WorkProfile')
    current_profile = models.ForeignKey('WorkProfile', models.SET_NULL, null=True, related_name="current_work_profile")
    current_class = models.ForeignKey('Classes.Class', models.SET_NULL, null=True)
    current_stream = models.ForeignKey('Streams.Stream', models.SET_NULL, null=True)
    Lessons = models.ManyToManyField('Lessons.Lesson', blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class WorkProfile(models.Model):
    Teacher = models.ForeignKey('Teacher', models.SET_NULL, null=True)
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Classes = models.ManyToManyField('Classes.Class', blank=True)
    Stream = models.ForeignKey('Streams.Stream', models.SET_NULL, null=True)
    Subjects = models.ManyToManyField('Subjects.Subject')
    Lessons = models.ManyToManyField('Lessons.Lesson', blank=True)