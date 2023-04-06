from django.db import models
from django.utils.timezone import now

programmes = (
    ('Scholarship', 'Scholarship'),
    ('Sponsored', 'Sponsored'),
    ('Full Bursary', 'Full Bursary'),
    ('Half Bursary', 'Half Bursary'),
)

class Enrollment(models.Model):
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Student = models.ForeignKey('Students.Student', models.CASCADE)
    Programme = models.CharField(max_length=100, choices=programmes, null=True)
    Date = models.DateTimeField(default=now)

