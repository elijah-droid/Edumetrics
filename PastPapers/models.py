from django.db import models
from Subjects.models import subjects
from Classes.models import classes
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now


class PastPaper(models.Model):
    Paper = models.ForeignKey('Examinations.Paper', models.SET_NULL, null=True)
    Questions_Pdf = models.FileField(upload_to='PastPapers/Papers', validators=[FileExtensionValidator(['pdf'])])
    Answers_Pdf = models.FileField(upload_to='PastPapers/Answers', validators=[FileExtensionValidator(['pdf'])], null=True, blank=True)
    Downloads = models.PositiveIntegerField(default=0)
    Date = models.DateTimeField(default=now)
                                 