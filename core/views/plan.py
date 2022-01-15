from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from core.models import Thing, UserProfile, Plan
from core.mixins import LoginRequiredMixin, IsThePlanOwner
from core.decorators import is_plan_owner

@is_plan_owner
def plan_add(request, plan_pk, thing_pk):
    plan = Plan.objects.get(pk=plan_pk)
    thing = Thing.objects.get(pk=thing_pk)
    
    if thing in plan.things.all():
        messages.warning(request, f'Thing "{thing.name}" is already in plan "{plan.name}"')

    else:
        plan.things.add(thing)
        messages.success(request, f'Successfully added thing "{thing.name}" to plan "{plan.name}"')

    return HttpResponseRedirect(reverse('core:thing_detail', kwargs={'pk': thing.pk}))

@is_plan_owner
def plan_remove(request, plan_pk, thing_pk):
    plan = Plan.objects.get(pk=plan_pk)
    thing = Thing.objects.get(pk=thing_pk)
    plan.things.remove(thing)

    messages.success(request, f'Successfully removed thing "{thing.name}" from plan "{plan.name}"')

    return HttpResponseRedirect(reverse('core:user_detail', kwargs={'pk': plan.owner.pk}) + "?my_plans")

@login_required
def plan_like(request, user_pk, plan_pk, liking):
    user = UserProfile.objects.get(pk=user_pk)
    plan = Plan.objects.get(pk=plan_pk)
    
    if liking == 'true':
        user.likes.add(plan)
        messages.success(request, f'Successfully liked plan "{plan.name}"')
    
    else:
        user.likes.remove(plan)
        messages.error(request, f'Successfully disliked plan "{plan.name}"')

    return HttpResponseRedirect(reverse('core:user_detail', kwargs={'pk': plan.owner.pk}) + "?my_plans")

class PlanCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'description', 'is_public']
    model = Plan
    template_name = 'core/plan/form.html'

    def form_valid(self, form):
        form.instance.owner = UserProfile.objects.get(id=int(self.kwargs['owner_pk']))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, f'Successfully created plan "{self.object.name}", now add a thing to it.')

        thing = self.request.GET.get('thing')
        if thing:
            return reverse(f"core:thing_detail", kwargs={"pk": thing})

        return reverse(f"core:user_detail", kwargs={"pk": self.object.owner.pk}) + "?my_plans"

class PlanUpdateView(IsThePlanOwner, UpdateView):
    login_url = 'core:user_login'
    fields = ['name', 'description', 'is_public']
    model = Plan
    template_name = 'core/plan/form.html'

    def form_valid(self, form):
        return super().form_valid(form)

class PlanDeleteView(IsThePlanOwner, DeleteView):
    login_url = 'core:user_login'
    model = Plan
    template_name = 'core/plan/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(f"core:user_detail", kwargs={'pk': self.get_object().owner.id}) + "?my_plans"