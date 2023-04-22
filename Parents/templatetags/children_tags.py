from django.urls import reverse
from Reports.models import Report
from FeesManagement.templatetags import fees_tags
from Events.models import Event
from django import template

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


@register.filter
def parent_reports(parent):
    reports = Report.objects.filter(Student__in=parent.relationships.values('Child'), Published=True)
    return reports

@register.filter
def parent_events(parent):
    events = Event.objects.filter(school__in=parent.relationships.values('Child__school'), Classes__in=parent.relationships.values('Child__Class')).distinct()
    return events

@register.filter
def total_fees_balance(parent):
    total = 0
    for relationship in parent.relationships.all():
        balance = fees_tags.fees_balance(relationship.Child)
        try:
            int(balance)
            total += balance
        except:
            pass
        return balance
