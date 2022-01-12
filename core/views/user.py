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
            
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserProfileForm()

    if registered:
        return HttpResponseRedirect(reverse('core:user_login') + '?new_user')

    else:
        return render(request,
            'core/user/registration.html',
            {'user_form': user_form,})

def user_login(request):
    next_page = request.GET.get('next')
    if next_page:
        messages.warning(request, 'Login is required for that action')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if next_page:
                    next_page = next_page.split('?')
                    if len(next_page) > 1:
                        view_name = next_page[0][1:-1].replace('/', ':', 1).replace('/', '_')
                        querystring = '&'.join(next_page[1:])
                        return HttpResponseRedirect(f"{reverse(view_name)}?{querystring}")
            
                    return HttpResponseRedirect(reverse(next_page[1:-1].replace('/', ':', 1).replace('/', '_')))
                return HttpResponseRedirect(reverse('index'))

            else:
                messages.error(request,'Account not active')

        else:
            messages.error(request,'Invalid credentials')
        
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