from django.db import models

classes = (
    ('Baby', 'Baby'),
    ('Middle', 'Middle'),
    ('Top', 'Top'),
    ('Primary One', 'Primary One'),
    ('Primary Two', 'Primary Two'),
    ('Primary Three', 'Primary Three'),
    ('Primary Four', 'Primary Four'),
    ('Primary Five', 'Primary Five'),
    ('Primary Six', 'Primary Six'),
    ('Primary Seven', 'Primary Seven'),
    ('Senior One', 'Senior One'),
    ('Senior Two', 'Senior Two'),
    ('Senior Three', 'Senior Three'),
    ('Senior Four', 'Senior Four'),
    ('Senior Five', 'Senior Five'),
    ('Senior Six', 'Senior Six')
)

class Class(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Name = models.CharField(max_length=100, choices=classes)
    Index = models.PositiveIntegerField(default=1)
    Class_Teacher = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True, blank=True)
    Streams = models.ManyToManyField('Streams.Stream')
    Students = models.ManyToManyField('Students.Student', blank=True)
    From = models.TimeField(null=True, blank=True)
    To = models.TimeField(null=True, blank=True)
    Lessons = models.ManyToManyField('Lessons.Lesson', blank=True)

    def __str__(self):
        return self.Name

    class META:
        unique_together = ('School', 'Name')