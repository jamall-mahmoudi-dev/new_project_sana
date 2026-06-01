
from django import template
import datetime


register = template.Library()

@register.simple_tag
def zarb(a, b):
    return a * b

@register.filter
def filtering(value):
    return value

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)