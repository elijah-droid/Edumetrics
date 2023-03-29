from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Crop


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = ProcessedImageField(
        upload_to='Students/Photos',
        processors=[ResizeToFill(200, 200), Crop(200, 200)],
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True
    )
    parents = models.ManyToManyField('Parents.Parent', blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    school = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Class = models.ForeignKey('Classes.Class', models.SET_NULL, null=True)
    Subjects = models.ManyToManyField('Subjects.Subject', blank=True)
    Reports = models.ManyToManyField('Reports.Report', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name