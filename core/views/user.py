from django.shortcuts import render
from django import forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView

from core.models import User, UserProfileInfo
from core.forms import UserForm, UserProfileInfoForm

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False) # avoid collissions with user
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    if registered:
        return HttpResponseRedirect(reverse('core:user_login') + '?new_user')

    else:
        return render(request,
            'core/user/registration.html',
            {'user_form': user_form,
             'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print("FAILED LOGIN")
            return HttpResponse('INVALID LOGIN DETAILS')

    else:
        return render(request, 'core/user/login.html')

class UserDetailView(DetailView):
    context_object_name = "user_detail"
    model = User
    template_name = 'core/user/detail.html'

class UserUpdateView(UpdateView):
    fields = ['biography', 'profile_pic']
    model = UserProfileInfo
    template_name = 'core/user/form.html'

    def form_valid(self, form):
        if not form.instance.profile_pic:
            form.instance.profile_pic = 'profile_pics/default.jpg'
        
        return super().form_valid(form)