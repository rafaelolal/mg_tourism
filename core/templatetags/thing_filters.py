from typing import Any

from django import template
from django.forms.models import model_to_dict

from core.models import Thing, Attraction, Outdoor, Shopping, Food, Tour

register = template.Library()

@register.filter
def to_int(value: str) -> int:
    return round(float(value))

@register.filter
def to_str(value: Any) -> str:
    return str(value)

@register.filter
def add_spaces(value): # Only one argument.
    return value.replace('_', ' ').title()

@register.simple_tag
def is_checked(category, checked):
    if category in checked:
        if checked[category] == 'on':
            return 'checked'

@register.simple_tag
def any_query(checked):
    return any(checked.values())

@register.simple_tag
def get_param_value(param, query):
    if param in query:
        if query[param] != '0' and query[param] != '' and query[param] != 'Any':
            return query[param].replace('_', ' ')

    return ''

@register.simple_tag
def is_in_query(categories, query):
    categories = categories.split(' ')
    return any([category in query for category in categories]) or all([category not in query for category in Thing.categories])

@register.simple_tag
def my_get_field(field, thing):
    category = thing.category
    return eval(f'thing.{category}.{field}'.lower())

@register.simple_tag
def get_field_value(field, thing):
    return getattr(eval(f'thing.{str(thing.category).lower()}'), field)

@register.simple_tag
def get_good_fors(things):
    good_fors = []
    for thing in things:
        category = getattr(thing, 'category').lower()
        fields = set(model_to_dict(eval(f'thing.{category}')))
        if 'good_for' in fields:
            thing_good_for = getattr(eval(f'thing.{category}'), 'good_for')
            if thing_good_for not in good_fors:
                good_fors.append(thing_good_for)
    
    return good_fors

@register.simple_tag
def get_types(things):
    types = []
    for thing in things:
        category = getattr(thing, 'category').lower()
        fields = set(model_to_dict(eval(f'thing.{category}')))
        if 'type' in fields:
            thing_type = getattr(eval(f'thing.{category}'), 'type')
            if thing_type not in types:
                types.append(thing_type)
    
    return types

@register.simple_tag
def get_thing(query):
    id = int(query['thing'])
    return Thing.objects.get(id=id)