from django import template
from django.urls import reverse

register = template.Library()

@register.filter
def relationships(parent, school):
    relationships = parent.relationships.filter(Child__school=school)
    return relationships

@register.filter
def relationship(child, parent):
    try:
        relationship = parent.relationships.get(Child=child)
        return relationship.Relationship
    except:
        return ''
