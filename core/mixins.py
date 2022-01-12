# source: https://stackoverflow.com/questions/67351312/django-check-if-superuser-in-class-based-view

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class IsTheUser(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])