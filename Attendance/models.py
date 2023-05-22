from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Attendance(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True, related_name='daily_attendance')
    Date = models.DateField(default=now)
    Class = models.ForeignKey('Classes.Class', models.SET_NULL, null=True)
    Students = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('Date', 'School', 'Class')


class RollCall(models.Model):
    Date = models.DateTimeField(default=now)
    Lesson = models.ForeignKey('Lessons.Lesson', models.CASCADE)
    Attendees = models.ManyToManyField('Students.Student', blank=True) 