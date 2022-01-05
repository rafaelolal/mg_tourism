from django import template

register = template.Library()

@register.filter
def remove_spaces(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.replace(' ', '_')

@register.simple_tag
def is_checked(category, checked):
    if category in checked:
        if checked[category] == 'on':
            return 'checked'

@register.simple_tag
def any_query(checked):
    return any(checked.values())

@register.simple_tag
def get_min_stars(query):
    if 'min_stars' in query:
        return query['min_stars']
    return '0'

@register.simple_tag
def is_in_query(category, query):
    query = [k.lower() for k in query.keys()]
    return category in query