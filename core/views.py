from typing import final
from django.db.models import query
from django.shortcuts import render
from django import forms

# login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
    DetailView, CreateView,
    UpdateView, DeleteView)

from core.models import Thing, Attraction, Tour, Picture
from core.forms import UserForm, UserProfileInfoForm

class IndexView(TemplateView):
    template_name = 'core/index.html'

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
            raise forms.ValidationError('INVALID FORM')

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,
        'core/registration.html',
        {
            'registered': registered,
            'user_form': user_form,
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
        return render(request, 'core/user_login.html')

class AttractionCreateView(CreateView):
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'neighborhood', 'good_for']
    model = Attraction

    def form_valid(self, form):
        form.instance.category = 'Attraction'
        return super().form_valid(form)

class ThingDetailView(DetailView):
    # returns model name in lowercase
    # better to change it yourself:
    context_object_name = "thing_detail"
    model = Thing
    template_name = 'core/thing_detail.html'

class TourCreateView(CreateView):
    fields = ['name', 'short_description', 'long_description', 'address', 'covid_safe', 'type', 'price', 'duration']
    model = Tour

    def form_valid(self, form):
        form.instance.category = 'Tour'
        return super().form_valid(form)

class ThingListView(ListView):
    model = Thing

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs,
        categories=self.model.categories,
        good_fors=Attraction.good_fors)

    def get_queryset(self):
        query_paremeters = self.get_query_parameters()
        return self.query_filter(query_paremeters)

    def get_query_parameters(self):
        querystring = []
        for category in self.model.categories:
            querystring.append(self.convert_on(self.request.GET.get(category.lower().replace(' ', '_'))))

        return querystring

    @staticmethod
    def convert_on(category):
        if category == 'on':
            return 'checked'
        return ''

    def query_filter(self, querystring):
        queryset = []
        print(self.request.GET)
        for category, param in zip(self.model.categories, querystring):
            print(category, 'category in query')
            print(param, 'param in query')
            if param:
                queryset.append(Thing.objects.filter(category=category))

        if queryset:
            return self.combine(queryset)

        else:
            return Thing.objects.all()

    @staticmethod
    def combine(queryset):
        final_queryset = queryset[0]
        for query in queryset[1:]:
            final_queryset = final_queryset | query

        return final_queryset

# TODO if this was a class I could have all these methods namespaced
# def things(request):
#     # all attributes
#     stars = None
#     # attraction and tour
#     types = []

#     # attraction
#     neighborhood = False
#     good_for = []

#     # tour
#     price = None
#     duration = None

#     categories = ['Attraction', 'Tour', 'Food', 'Outdoor Activities', 'Shopping']

#     querystring = get_querystring(request, categories)
#     t_things = filter_(categories, querystring)
#     final_things = combine(t_things)

#     if any(querystring):
#         stars = True

#     if querystring[0]:
#         types += Attraction.types
#         neighborhood = True
#         good_for += Attraction.good_for_choices

#     if querystring[1]:
#         types += Tour.types
#         tours = Tour.objects
        
#         by_price = tours.order_by('price')
#         lowest_price = by_price[0].price
#         highest_price = by_price[len(list(tours.all()))-1].price
#         price = (lowest_price, highest_price)

#         by_duration = tours.order_by('duration')
#         shortest_duration = by_duration[0].duration
#         longest_duration = by_duration[len(list(tours.all()))-1].duration

#         duration = (shortest_duration, longest_duration)

#     context = {'things': final_things,
#         'stars': stars,
#         'types': types,
#         'neighborhood': neighborhood,
#         'good_for': good_for,
#         'price': price,
#         'duration': duration,} | get_params(categories, querystring)

#     return render(request, 'core/things.html', context=context)

class PictureCreateView(CreateView):
    fields = ['image']
    model = Picture

    def form_valid(self, form):
        thing = self.request.GET['thing']
        t = Thing.objects.get(id=thing)
        form.instance.thing = t
        return super().form_valid(form)