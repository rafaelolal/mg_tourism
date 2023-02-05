"""Views associated with Plan objects"""

from django.forms import Form

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Thing, UserProfile, Plan
from core.mixins import LoginRequiredMixin, IsThePlanOwner
from core.decorators import is_plan_owner

@is_plan_owner
def plan_add(request: HttpResponse, plan_pk: int, thing_pk: int) -> HttpResponse:
    """Adds a Thing object to a Plan
    Checks if the Thing is already in the Plan and returns a message accordingly
    Redirects user back to the Thing's detail view
    """

    plan = Plan.objects.get(pk=plan_pk)
    thing = Thing.objects.get(pk=thing_pk)
    
    if thing in plan.things.all():
        messages.warning(request, f'Thing "{thing.name}" is already in plan "{plan.name}"')

    else:
        plan.things.add(thing)
        messages.success(request, f'Successfully added "{thing.name}" to "{plan.name}"')

    return HttpResponseRedirect(reverse('core:thing_detail', kwargs={'pk': thing.pk}))

@is_plan_owner
def plan_remove(request: HttpResponse, plan_pk: int, thing_pk: int) -> HttpResponse:
    """Removes a Thing object from a Plan
    Redirects user back to their detail view on the "My Plans" tab
    """

    plan = Plan.objects.get(pk=plan_pk)
    thing = Thing.objects.get(pk=thing_pk)
    plan.things.remove(thing)

    messages.success(request, f'Successfully removed "{thing.name}" from "{plan.name}"')

    return HttpResponseRedirect(request.GET.get('next'))

@login_required
def plan_favorite(request: HttpResponse, plan_pk: int) -> HttpResponse:
    """Favorites or unfavorites a plan depending if the user has already favorited this plan
    Redirects user back to the view they favorited the plan in
    """

    user = UserProfile.objects.get(pk=request.user.pk)
    plan = Plan.objects.get(pk=plan_pk)
    
    if not plan in user.favorited.all():
        user.favorited.add(plan)
        messages.success(request, f'Successfully favorited "{plan.name}"')


    else:
        user.favorited.remove(plan)
        messages.success(request, f'Successfully disfavorited "{plan.name}"')

    if request.GET.get('next') == '/':
        return HttpResponseRedirect(request.GET.get('next') + "#plans")

    return HttpResponseRedirect(request.GET.get('next'))
    
    
class PlanCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'description', 'is_public']
    model = Plan
    template_name = 'core/plan/form.html'

    def form_valid(self, form: Form) -> HttpResponse:
        """Manually sets the owner attribute of a Plan object to the UserProfile object with the matchin pk given in the request"""
        
        form.instance.owner = UserProfile.objects.get(pk=int(self.request.user.pk))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        """Gets the HttpResponse object the user is supposed to be redirected to after creating a plan
        Sends the user back to the Thing detail view they created the project on, else redirects back to their profile view
        """

        messages.success(self.request, f'Successfully created "{self.object.name}", now add something to it.')

        thing = self.request.GET.get('thing')
        if thing:
            return reverse(f"core:thing_detail", kwargs={"pk": thing})

        return reverse(f"core:user_detail", kwargs={"pk": self.object.owner.pk}) + "?my_plans"

class PlanUpdateView(IsThePlanOwner, UpdateView):
    login_url = 'core:user_login'
    fields = ['name', 'description', 'is_public']
    model = Plan
    template_name = 'core/plan/form.html'

    def form_valid(self, form: Form) -> HttpResponse:
        """Checks if the plan is no longer public and removes all UserProfile objects which favorited it"""

        if not form.instance.is_public:
            form.instance.favorited_by.clear()

        return super().form_valid(form)

class PlanDeleteView(IsThePlanOwner, DeleteView):
    login_url = 'core:user_login'
    model = Plan
    template_name = 'core/plan/confirm_delete.html'

    def get_success_url(self) -> HttpResponse:
        """Redirects user back to their profile view in the "My Plans" tab after deleting a plan"""

        return reverse_lazy(f"core:user_detail", kwargs={'pk': self.get_object().owner.pk}) + "?my_plans"