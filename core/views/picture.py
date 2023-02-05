"""Views associated with Picture objects"""

from django.views.generic import CreateView

from core.models import Thing, Picture
from core.mixins import LoginRequiredMixin

class PictureCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['image']
    model = Picture

    def form_valid(self, form):
        """Checks if the form is valid
        Manually sets the thing attribute of a Picture object to the Thing with the matching pk given in the request
        """

        thing = Thing.objects.get(pk=int(self.kwargs['thing_pk']))
        form.instance.thing = thing
        return super().form_valid(form)