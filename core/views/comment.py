from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Thing, UserProfile, Comment
from core.mixins import IsTheCommentAuthor, IsFirstComment

class CommentCreateView(IsFirstComment, CreateView):
    login_url = 'core:user_login'
    fields = ['title', 'content']
    model = Comment
    template_name = 'core/comment/form.html'

    # manually change some things on the form before submitting it
    def form_valid(self, form):
        thing = Thing.objects.get(id=int(self.kwargs['thing_pk']))
        
        form.instance.thing = thing
        form.instance.author = UserProfile.objects.get(id=self.request.user.id)
        
        form.instance.rating = int(self.request.POST.get('rating'))

        return super().form_valid(form)

class CommentUpdateView(IsTheCommentAuthor, UpdateView):
    login_url = 'core:user_login'
    fields = ['title', 'content']
    model = Comment
    template_name = 'core/comment/form.html'

    def form_valid(self, form):
        form.instance.is_edited = True    
        form.instance.rating = int(self.request.POST.get('rating'))
    
        return super().form_valid(form)

class CommentDeleteView(IsTheCommentAuthor, DeleteView):
    login_url = 'core:user_login'
    model = Comment
    template_name = 'core/comment/confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(f"core:thing_detail", kwargs={'pk': self.get_object().thing.id})