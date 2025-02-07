from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Custom filter to safely get dictionary values in Django templates."""
    return dictionary.get(key, 0)