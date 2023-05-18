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
    ('Islamic Religious Education', 'Islamic Religious Education'),
    ('History', 'History'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Turkish', 'Turkish')
)

subject_types = (
    ('Compulsory', 'Compulsory'),
    ('Optional', 'Optional')
)


class Subject(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    name = models.CharField(max_length=100, choices=subjects)
    code = models.CharField(max_length=10)
    description = models.TextField()
    Head_Of_Department = models.ForeignKey('Teachers.Teacher', models.SET_NULL, null=True, related_name='HOD', blank=True)
    Teachers = models.ManyToManyField('Teachers.Teacher')
    Students = models.ManyToManyField('Students.Student')
    Levels = models.ManyToManyField('Levels.Level', blank=True)
    Type = models.CharField(max_length=100, choices=subject_types, null=True)


    def __str__(self):
        return self.name


class Combination(models.Model):
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Name = models.CharField(max_length=100, null=True)
    Principals = models.ManyToManyField('Subjects.Subject', blank=True)
    Subsidiary = models.ForeignKey('Subjects.Subject', models.CASCADE, related_name='subsidiary')
    Students = models.ManyToManyField('Students.Student', blank=True)