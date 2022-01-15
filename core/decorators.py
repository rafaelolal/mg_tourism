from django.core.exceptions import PermissionDenied
from core.models import Plan

def is_plan_owner(function):
    def wrapper(request, *args, **kwargs):
        plan = Plan.objects.get(pk=kwargs['plan_pk'])
        if request.user.pk == plan.owner.pk:
            return function(request, *args, **kwargs)
    
        else:
            raise PermissionDenied

    return wrapper