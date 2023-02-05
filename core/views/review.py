"""Views associated with Review objects"""

from django.forms import Form
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Thing, UserProfile, Review
from core.mixins import IsTheReviewAuthor, IsFirstReview

class ReviewCreateView(IsFirstReview, CreateView):
    login_url = 'core:user_login'
    fields = ['title', 'content']
    model = Review
    template_name = 'core/review/form.html'

    def form_valid(self, form: Form) -> HttpResponse:
        """Manually sets the thing, author, and rating for a review
        Thing and author come from the request
        Rating comes from the request's POST, needed because I create my own input for rating
        """

        thing = Thing.objects.get(pk=int(self.kwargs['thing_pk']))
        
        form.instance.thing = thing
        form.instance.author = UserProfile.objects.get(pk=self.request.user.pk)
        
        form.instance.rating = int(self.request.POST.get('rating'))

        return super().form_valid(form)

class ReviewUpdateView(IsTheReviewAuthor, UpdateView):
    login_url = 'core:user_login'
    fields = ['title', 'content']
    model = Review
    template_name = 'core/review/form.html'

    def form_valid(self, form: Form) -> HttpResponse:
        """Manually sets the is_edited field and gets the rating field from the request's POST"""

        form.instance.is_edited = True    
        form.instance.rating = int(self.request.POST.get('rating'))
    
        return super().form_valid(form)

class ReviewDeleteView(IsTheReviewAuthor, DeleteView):
    login_url = 'core:user_login'
    model = Review
    template_name = 'core/review/confirm_delete.html'

    def get_success_url(self) -> HttpResponse:
        """Redirects the user back to the Thing's detail view they deleted the review from"""

        return reverse_lazy(f"core:thing_detail", kwargs={'pk': self.get_object().thing.pk})