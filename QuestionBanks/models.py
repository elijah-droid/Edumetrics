from django.db import models
from Subjects.models import subjects

levels = (
    ('PLE', 'PLE'),
    ('UCE', 'UCE'),
    ('UACE', 'UACE'),
)

class QuestionBank(models.Model):
    Year = models.PositiveIntegerField()
    Subject = models.CharField(max_length=100, choices=subjects)
    Level = models.CharField(max_length=10, choices=levels)
    Potable_Digital_Formart = models.FileField(upload_to='QuestionBanks/pdf', null=True)
