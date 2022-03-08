"""Mixins for class based views
Mixins are a way to validate if a user can access a view
and will redirect to a 403 forbidden page if access is denied
"""

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Review, UserProfile, Plan

class IsSuperuserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is a superuser
    Will redirect the user to a view's login_url attribute if they are not logged in
    """

    def test_func(self) -> bool:
        return self.request.user.is_superuser

class IsTheUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is associated with the view
    Will redirect the user to a view's login_url attribute if they are not logged in
    """
    
    def test_func(self) -> bool:
        return self.request.user.pk == int(self.kwargs['pk'])

class IsTheReviewAuthor(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is the author of the review associated with the view
    Will redirect the user to a view's login_url attribute if they are not logged in
    """

    def test_func(self) -> bool:
        return self.request.user.pk == Review.objects.get(pk=int(self.kwargs['pk'])).author.pk

class IsThePlanOwner(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is the owner of the plan associated with the view
    Will redirect the user to a view's login_url attribute if they are not logged in
    """

    def test_func(self) -> bool:
        return self.request.user.pk == Plan.objects.get(pk=int(self.kwargs['pk'])).owner.pk

class IsFirstReview(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is the owner of the plan associated with the view
    Checks if a user has already reviewed on the post associated with the view"""

    def test_func(self) -> bool:
        return not UserProfile.objects.get(pk=self.request.user.pk).reviews.filter(thing__pk=int(self.kwargs['thing_pk'])).exists()