from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView

from core.models import UserProfile
from core.forms import UserProfileForm
from core.mixins import IsTheUser

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            
            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
            
            if not user.first_name:
                user.first_name = user.username.capitalize()

            if not user.last_name:
                user.last_name = 'User'

            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserProfileForm()

    if registered:
        next_page = request.GET.get('next')
        if next_page:
            return HttpResponseRedirect(reverse('core:user_login') + f'?next={next_page}' + '&new_user')

        return HttpResponseRedirect(reverse('core:user_login') + '?new_user')

    else:
        return render(request,
            'core/user/registration.html',
            {'user_form': user_form,})

def user_login(request):
    next_page = request.GET.get('next')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if next_page:
                    return HttpResponseRedirect(next_page)
            
                return HttpResponseRedirect(reverse('index'))

            else:
                messages.error(request,'Account not active')

        else:
            messages.error(request,'Invalid credentials')
        
    else:
        if next_page:
            messages.warning(request, 'Login is required for that action')

    return render(request, 'core/user/login.html')

class UserDetailView(DetailView):
    context_object_name = "user_detail"
    model = UserProfile
    template_name = 'core/user/detail.html'

class UserUpdateView(IsTheUser, UpdateView):
    login_url = 'core:user_login'
    fields = ['biography', 'profile_pic']
    model = UserProfile
    template_name = 'core/user/form.html'

    def form_valid(self, form):
        if not form.instance.profile_pic:
            form.instance.profile_pic = 'profile_pics/default.jpg'
        
        return super().form_valid(form)

class UserDeleteView(IsTheUser, DeleteView):
    login_url = 'core:user_login'
    model = UserProfile
    template_name = 'core/user/confirm_delete.html'
    success_url = reverse_lazy("index")