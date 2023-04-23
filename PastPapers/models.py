from django.db import models
from Subjects.models import subjects
from Classes.models import classes
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now


class PastPaper(models.Model):
    Teacher = models.ForeignKey('Teachers.Teacher', models.CASCADE)
    Class = models.CharField(max_length=20, choices=classes, null=True)
    Subject = models.CharField(max_length=100, choices=subjects)
    Questions_Pdf = models.FileField(upload_to='PastPapers/Papers', validators=[FileExtensionValidator(['pdf'])])
    Answers_Pdf = models.FileField(upload_to='PastPapers/Answers', validators=[FileExtensionValidator(['pdf'])], null=True, blank=True)
    Description = models.TextField(max_length=1000)
    Price = models.PositiveIntegerField()
    Downloads = models.PositiveIntegerField(default=0)
    Date = models.DateTimeField(default=now)
