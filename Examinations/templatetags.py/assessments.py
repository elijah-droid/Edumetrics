from django import template

register = template.Library()

@register.simple_tag3
def get_score():
    return "Hello, World!"
