"""Custom tags to be used in django templates
Tags are functions that can be used within a template
"""

from typing import Dict, List, Union
from django.db.models.query import QuerySet

from django import template
from django.forms.models import model_to_dict
from django.db.models import Count

from core.models import (Thing, Attraction, Outdoor, Shopping, Food, Tour,
    UserProfile, Plan)

register = template.Library()

@register.simple_tag
def get_all_things() -> QuerySet:
    """Returns a QuerySet object with all Thing objects"""

    return Thing.objects.all()

@register.simple_tag
def get_top_things() -> QuerySet:
    """Returns a QuerySet object with the top 3 things by review count"""

    return Thing.objects.annotate(review_count=Count('reviews')).order_by('-review_count')[:3]

@register.simple_tag
def is_checked(select_filter: str, checked: Dict[str, str]) -> Union[None, str]:
    """Checks if a switch filter is checked"""

    if select_filter in checked:
        if checked[select_filter] == 'on':
            return 'checked'

@register.simple_tag
def any_query(checked: Dict[str, str]) -> bool:
    """Checks if any switch is checked"""

    return any(checked.values())

@register.simple_tag
def get_param_value(param: str, query: Dict[str, str]) -> str:
    """Checks if a parameter is being filtered for and returns its value or an empty string"""

    if param in query:
        if query[param] != '0' and query[param] != '' and query[param] != 'Any':
            return query[param].replace('_', ' ')

    return ''

@register.simple_tag
def is_in_query(categories: str, query: Dict[str, str]) -> bool:
    """Checks if a the given categories are being filtered for"""

    categories = categories.split(' ')
    return any([category in query for category in categories]) or all([category not in query for category in Thing.categories])

@register.simple_tag
def get_field_value(field: str, thing: Thing) -> 'str':
    """Gets the value of a field of a Thing object independent of its category"""

    return getattr(eval(f'thing.{str(thing.category).lower()}'), field)

@register.simple_tag
def get_good_fors(things: QuerySet) -> List[str]:
    """Returns all the good fors possible of Thing objects available"""

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
def get_types(things: QuerySet) -> List[str]:
    """Returns all types possible for Thing objects available"""

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
def get_thing(pk: int) -> Thing:
    """Returns a Thing object with the given pk"""

    return Thing.objects.get(pk=pk)

@register.simple_tag
def get_things_near(thing: Thing) -> QuerySet:
    """Returns up to 5 Thing objects that match the given neighborhood"""

    categories = Thing.categories.copy()
    categories.remove('Tour')
    things = None
    for category in categories:
        if not things:
            things = Thing.objects.all().filter(**{f'{category.lower()}__neighborhood': eval(f'thing.{thing.category.lower()}.neighborhood')})
        else:
            things |= Thing.objects.all().filter(**{f'{category.lower()}__neighborhood': eval(f'thing.{thing.category.lower()}.neighborhood')})
    
    return things.exclude(pk=thing.pk)

@register.simple_tag
def get_owner(pk: int) -> UserProfile:
    """Returns a UserProfile object with the given pk"""
    return UserProfile.objects.get(pk=pk)

@register.simple_tag
def user_reviewed(user_pk: int, thing_pk: int) -> bool:
    """Checks wether a user has reviewed on a thing"""

    if UserProfile.objects.get(pk=user_pk).reviews.filter(thing__pk=thing_pk).exists():
        return True

    return False

@register.simple_tag
def user_favorited(user_pk: int, plan_pk: int) -> bool:
    """Checks wether a user has favorited a plan"""

    if Plan.objects.get(pk=plan_pk) in UserProfile.objects.get(pk=user_pk).favorited.all():
        return True

    return False

@register.simple_tag
def get_plans(user_pk: int) -> QuerySet:
    """Returns all the plans a UserProfile object with the given pk has associated with it"""

    return UserProfile.objects.get(pk=int(user_pk)).plans.all

@register.simple_tag
def get_top_plans() -> QuerySet:
    """Returns a QuerySet object of the top 5 plans by favorites"""

    return Plan.objects.annotate(favorited_count=Count('favorited_by')).order_by('-favorited_count')[:5]

@register.simple_tag
def any_tab_selected(query: Dict[str, str]) -> str:
    """Checks wether the user is looking at a tab other than the main "Visited" tab on a UserProfile detail view"""

    if 'my_plans' in query or 'favorited_plans' in query:
        return ""
    
    return 'show active'

@register.simple_tag
def is_tab_selected(tab: str, query: Dict[str, str]) -> str:
    """Checks if a specific tab in a UserProfile detail view is active"""

    if tab in query:
        return "show active"

    return ""

@register.simple_tag
def get_visible_plans(plans: QuerySet, user_viewing_pk: int, user_detail_pk: int) -> QuerySet:
    """Returns the plans a user is allowed to view depending if they are the owner or if it is private"""

    if user_viewing_pk == user_detail_pk:
        return plans
    
    else:
        return plans.exclude(is_public=False)

@register.simple_tag
def get_sorts() -> List[str]:
    """Returns all sorts possible"""

    sorts = ['Quality', 'Popularity']
    return sorts

@register.simple_tag
def things_sorted_by(sort_by: str, things: QuerySet) -> QuerySet:
    """Converts a sort option to the corresponding Thing field"""
    
    conversions = {'Name': 'name', 'Quality': 'stars', 'Popularity': 'reviews.count'}
    if not sort_by:
        things = things.order_by('name')

    elif sort_by == 'Popularity':
        things = things.annotate(review_count=Count('reviews')).order_by('review_count')
    
    else:
        things = things.order_by(conversions[sort_by])
    
    if sort_by in ('Quality', 'Popularity'):
        return things.reverse()

    return things