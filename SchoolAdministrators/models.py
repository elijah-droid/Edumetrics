from django.db import models
from django.contrib.auth.models import User, Permission


roles = (
    ('Super', 'Super'),
    ('Staff', 'Staff')
)

class SchoolAdministrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    schools = models.ManyToManyField('Schools.school')
    role = models.CharField(max_length=10, choices=roles, null=True)
    current_school = models.ForeignKey('Schools.School', models.SET_NULL, null=True, related_name='current_school')
    adminship = models.ManyToManyField('Adminship', blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Adminship(models.Model):
    Admin = models.ForeignKey('SchoolAdministrator', models.CASCADE, related_name='admin_ship')
    School = models.ForeignKey('Schools.School', models.CASCADE)
    permissions = models.ManyToManyField(
        Permission,
        limit_choices_to={'content_type__app_label__in': ['Reports', 'Examinations']},
        blank=True,
        related_name='my_model_permissions',
    )


