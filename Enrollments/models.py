from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

programmes = (
    ('Scholarship', 'Scholarship'),
    ('Sponsored', 'Sponsored'),
    ('Full Bursary', 'Full Bursary'),
    ('Half Bursary', 'Half Bursary'),
)

class Enrollment(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    By = models.ForeignKey('SchoolAdministrators.SchoolAdministrator', models.SET_NULL, null=True)
    Student = models.ForeignKey('Students.Student', models.CASCADE)
    Programme = models.CharField(max_length=100, choices=programmes, null=True)
    Date = models.DateTimeField(default=now)

