from django.db import models

subjects = (
    ('Reading', 'Reading'),
    ('Writing', 'Writing'),
    ('Drawing', 'Drawing'),
    ('Mathematics', 'Mathematics'),
    ('English', 'English'),
    ('Science', 'Science'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Computer Studies', 'Computer Studies'),
    ('Social Studies', 'Social Studies'),
    ('Geography', 'Geography'),
    ('Christian Religious Education', 'Christian Religious Education'),
    ('Islamic Religious Education', 'Islamic Religious Education')
)

class Subject(models.Model):
    name = models.CharField(max_length=100, choices=subjects)
    code = models.CharField(max_length=10)
    description = models.TextField()
    Head_Of_Department = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True, related_name='HOD', blank=True)
    Teachers = models.ManyToManyField('Teachers.Teacher')
    Students = models.ManyToManyField('Students.Student')


    def __str__(self):
        return self.name
