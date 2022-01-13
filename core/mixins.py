# source: https://stackoverflow.com/questions/67351312/django-check-if-superuser-in-class-based-view

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models.comment import Comment, UserProfile

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class IsTheUser(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class IsTheCommentAuthor(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == Comment.objects.get(id=int(self.kwargs['pk'])).author.id

class IsFirstComment(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return not UserProfile.objects.get(id=self.request.user.pk).comment_set.filter(thing__id=int(self.request.GET.get('thing'))).exists()