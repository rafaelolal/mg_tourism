# source: https://stackoverflow.com/questions/67351312/django-check-if-superuser-in-class-based-view

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Comment, UserProfile, Plan

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class IsTheUser(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class IsTheCommentAuthor(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == Comment.objects.get(id=int(self.kwargs['pk'])).author.id

class IsThePlanOwner(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        if 'owner_pk' in self.kwargs:
            return self.request.user.pk == int(self.kwargs['owner_pk']) == Plan.objects.get(id=int(self.kwargs['pk'])).owner.pk
        else:
            return self.request.user.pk == Plan.objects.get(id=int(self.kwargs['pk'])).owner.pk

class IsFirstComment(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return not UserProfile.objects.get(id=self.request.user.pk).comment_set.filter(thing__id=int(self.kwargs['thing_pk'])).exists()