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
        categories=self.model.categories)

    def get_queryset(self):
        query_categories = self.get_query_categories()
        category_filtered = self.query_filter_categories(query_categories)
        query_fields = self.get_query_fields()
        return self.query_filter_fields(query_fields, category_filtered)

    def get_query_categories(self):
        querystring = []
        for category in self.model.categories:
            querystring.append(self.convert_on(self.request.GET.get(category)))

        return querystring

    def get_query_fields(self):
        query_fields = {}
        querystring = self.request.GET
        for query in querystring:
            if query not in self.model.categories and (querystring[query] and querystring[query] != 'Any'):
                query_fields[query] = querystring[query]

        return query_fields

    @staticmethod
    def convert_on(category):
        if category == 'on':
            return 'checked'
        return ''

    def query_filter_categories(self, query_categories):
        queryset = []
        for category, param in zip(self.model.categories, query_categories):
            if param:
                queryset.append(Thing.objects.filter(category=category))

        if queryset:
            return self.combine(queryset)

        else:
            return Thing.objects.all()

    def query_filter_fields(self, query_fields, things):
        if 'min_stars' in query_fields:
            things = things.filter(stars__gte=int(query_fields['min_stars']))

        tours = things.filter(category="Tour")
        others = things.filter(category__in=['Attraction', 'Food', 'Outdoor', 'Shopping'])
        for field in query_fields:
            if field in 'type max_price max_duration':
                if field == 'type':
                    tours = tours.filter(tour__type=query_fields[field].replace('_', ' '))
                elif field == 'max_price':
                    tours = tours.filter(tour__price__lte=int(query_fields[field]))
                elif field == 'max_duration':
                    tours = tours.filter(tour__duration__lte=int(query_fields[field]))
            if field in 'type neighborhood good_for':
                field_value = query_fields[field]
                if field == 'good_for':
                    field_value = query_fields[field].replace('_', ' ')
                    others = (others.filter(attraction__good_for=field_value)
                        | others.filter(food__good_for=field_value)
                        | others.filter(outdoor__good_for=field_value)
                        | others.filter(shopping__good_for=field_value))

                if field == 'type':
                    field_value = query_fields[field].replace('_', ' ')
                    others = (others.filter(attraction__type=field_value)
                        | others.filter(food__type=field_value)
                        | others.filter(outdoor__type=field_value)
                        | others.filter(shopping__type=field_value))

                elif field == 'neighborhood':
                    others = (others.filter(attraction__neighborhood=query_fields[field])
                        | others.filter(food__neighborhood=query_fields[field])
                        | others.filter(outdoor__neighborhood=query_fields[field])
                        | others.filter(shopping__neighborhood=query_fields[field]))

        return tours | others

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