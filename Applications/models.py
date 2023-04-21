from django.db import models
from django.utils.timezone import now

statuses = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved')
)

class Application(models.Model):
    Parent = models.ForeignKey('Parents.Parent', models.CASCADE)
    Student = models.ForeignKey('Students.Student', models.CASCADE, related_name="applicant")
    School = models.ForeignKey('Schools.School', models.SET_NULL, null=True)
    Date = models.DateTimeField(default=now)
    status = models.CharField(max_length=10, default='Pending')