from SchoolAdministrators.models import Adminship
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django import template

register = template.Library()

@register.filter()
def permissions(admin, school):
    permissions = Adminship.objects.get(Admin=admin, School=school).permissions.all()
    return permissions


@register.filter 
def groups(admin, school):
    adminship = Adminship.objects.get(Admin=admin, School=school)
    if adminship.super_admin:
        return ['Super User']
    else:
        return groups

@register.filter
def adminship(admin, school):
    adminship = Adminship.objects.get(Admin=admin, School=school)
    return adminship