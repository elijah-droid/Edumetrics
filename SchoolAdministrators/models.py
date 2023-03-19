from django.db import models
from django.contrib.auth.models import User


roles = (
    ('Super', 'Super'),
    ('Staff', 'Staff')
)

class SchoolAdministrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    schools = models.ManyToManyField('Schools.school')
    role = models.CharField(max_length=10, choices=roles, null=True)
    current_school = models.ForeignKey('Schools.School', models.SET_NULL, null=True, related_name='current_school')
    # other fields for the school administrator model

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

