from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Thing, UserProfile, Comment
from core.mixins import LoginRequiredMixin, IsTheUser

class CommentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['rating', 'title', 'content']
    model = Comment
    template_name = 'core/comment/form.html'

    # manually change some things on the form before submitting it
    def form_valid(self, form):
        t_id = self.request.GET['thing']
        thing = Thing.objects.get(id=t_id)
        
        form.instance.thing = thing
        form.instance.author = UserProfile.objects.get(id=self.request.user.id)
        
        return super().form_valid(form)

class CommentUpdateView(IsTheUser, UpdateView):
    login_url = 'core:user_login'
    fields = ['rating', 'title', 'content']
    model = Comment
    template_name = 'core/comment/form.html'

    def form_valid(self, form):
        form.instance.is_edited = True
        
        return super().form_valid(form)

class CommentDeleteView(IsTheUser, DeleteView):
    login_url = 'core:user_login'
    model = Comment
    template_name = 'core/comment/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(f"core:thing_detail", kwargs={'pk': self.get_object().thing.id})