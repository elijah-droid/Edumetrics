from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Crop

class School(models.Model):
    name = models.CharField(max_length=100)
    badge = ProcessedImageField(
        upload_to='Schools/Badges',
        processors=[ResizeToFill(200, 200), Crop(200, 200)],
        format='JPEG',
        options={'quality': 90},
        null=True, blank=True
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    mtn_account = models.PositiveIntegerField(null=True, blank=True)
    airtel_account =  models.PositiveIntegerField(null=True, blank=True)
    students = models.ManyToManyField('Students.Student', related_name='school_children', blank=True)
    classes = models.ManyToManyField('Classes.Class', blank=True)
    Events = models.ManyToManyField('Events.Event', blank=True, related_name='school_events')
    Examinations = models.ManyToManyField('Examinations.Examination', blank=True)
    Grades = models.ManyToManyField('Grading.Grade', blank=True)
    Divisions = models.ManyToManyField('Grading.Division', blank=True)
    Subjects = models.ManyToManyField('Subjects.Subject', blank=True)

    def __str__(self):
        return self.name
