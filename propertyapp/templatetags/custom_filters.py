from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """
    Generate a range of numbers up to the given value.
    """
    return range(value)
