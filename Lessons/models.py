from django.db import models
from django.utils.timezone import now

days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)

class Lesson(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Class = models.ForeignKey('Classes.Class', models.CASCADE)
    Day = models.CharField(max_length=100, choices=days)
    From = models.TimeField(null=True)
    To = models.TimeField(null=True)
    Subject = models.ForeignKey('Subjects.Subject', models.CASCADE)
    Teacher = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True)
    Roll_Calls = models.ManyToManyField('Attendance.RollCall')

    def __str__(self):
        return f'{self.Subject} {self.From}'

    class Meta:
        unique_together = ('School', 'Class', 'Teacher', 'Subject', 'Day')