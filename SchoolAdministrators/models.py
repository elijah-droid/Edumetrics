from django.db import models
from django.contrib.auth.models import User, Permission, Group
from django.utils.timezone import now

roles = (
    ('Super', 'Super'),
    ('Staff', 'Staff')
)

class SchoolAdministrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    schools = models.ManyToManyField('Schools.school', through='Adminship')
    role = models.CharField(max_length=10, choices=roles, null=True)
    current_school = models.ForeignKey('Schools.School', models.SET_NULL, null=True, related_name='current_school')
    adminship = models.ManyToManyField('Adminship', blank=True)

    def __str__(self):
        return f'{self.user.username}'


class Adminship(models.Model):
    Admin = models.ForeignKey('SchoolAdministrator', models.CASCADE, related_name='admin_ship')
    School = models.ForeignKey('Schools.School', models.CASCADE)
    Date_Authorised = models.DateTimeField(default=now)
    permissions = models.ManyToManyField(
        Permission,
        limit_choices_to={'content_type__app_label__in': ['Reports', 'Examinations']},
        blank=True,
        related_name='my_model_permissions',
    )
    Groups = models.ManyToManyField(Group, blank=True)
    super_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    unauthorized_attempts = models.PositiveBigIntegerField(default=0)

    class Meta:
        unique_together = ('Admin', 'School')

