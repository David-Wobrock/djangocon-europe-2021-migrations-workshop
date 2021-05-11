from django import template
from django.conf import settings

register = template.Library()


def hasattribute(value, arg):
    return hasattr(value, str(arg))


register.filter('hasattribute', hasattribute)
