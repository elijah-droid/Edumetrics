from django import template
from SchoolAdministrators.models import Adminship
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.filter()
def permissions(admin, school):
    permissions = Adminship.objects.get(Admin=admin, School=school).permissions.all()
    return permissions


@register.filter 
def groups(admin, school):
    groups = Adminship.objects.get(Admin=admin, School=school).Groups.all()
    return groups