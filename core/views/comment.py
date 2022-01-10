from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Thing, User, Comment

class CommentCreateView(CreateView):
    fields = ['rating', 'title', 'content']
    model = Comment
    template_name = 'core/comment/form.html'

    # manually change some things on the form before submitting it
    def form_valid(self, form):
        t_id = self.request.GET['thing']
        thing = Thing.objects.get(id=t_id)
        thing.calculate_stars(form.instance.rating)
        
        form.instance.thing = thing
        form.instance.author = User.objects.get(id=self.request.user.id)
        
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    fields = ['rating', 'title', 'content']
    model = Comment
    template_name = 'core/comment/form.html'

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'core/comment/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(f"core:thing_detail", kwargs={'pk': self.get_object().thing.id})