"""Custom filters to be used within django templates
Filters are functions used to change/format a value, usually for displaying purposes
"""

from typing import Any

from django import template

register = template.Library()

@register.filter
def to_int(value: str) -> int:
    """Converts strings to integers, even if the string is a float"""

    return round(float(value))

@register.filter
def to_str(value: Any) -> str:
    """Converts a value to a string"""

    return str(value)

@register.filter
def add_spaces(value: str) -> str:
    """Replaces underscores with spaces and capitalizes every word"""

    return value.replace('_', ' ').title()

@register.filter
def make_possessive(name: str) -> str:
    """Makes a name possessive by appropriately adding an apostrophe and s"""

    return name + ("'" if name[-1] == 's' else "'s")