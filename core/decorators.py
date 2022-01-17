"""Decorators used to check if a user has access to a view
Similar to mixins
"""

from typing import Callable

from django.core.exceptions import PermissionDenied
from core.models import Plan

def is_plan_owner(function: Callable) -> Callable:
    """Checks if the user is the owner of the plan associated with the view
    Raises a PermissionDenied error and redirects user to 403 Forbidden page if they are not the plan owner"""

    def wrapper(request, *args, **kwargs):
        plan = Plan.objects.get(pk=kwargs['plan_pk'])
        if request.user.pk == plan.owner.pk:
            return function(request, *args, **kwargs)
    
        else:
            raise PermissionDenied

    return wrapper