from typing import final
from django.shortcuts import render
from django import forms

# login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from core.models import Thing
from core.forms import UserForm, UserProfileInfoForm, AttractionForm, TourForm, ThingForm, PictureForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

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

def create_attraction(request):
    created = False

    if request.method == 'POST':
        thing_form = ThingForm(data=request.POST)
        attraction_form = AttractionForm(data=request.POST)
        pic_form = PictureForm(request.POST, request.FILES)

        print(thing_form.is_valid(), 'thing_form')
        print(attraction_form.is_valid(), 'attraction_form')
        print(pic_form.is_valid(), 'pic_form')

        if (thing_form.is_valid()
            and attraction_form.is_valid()
            and pic_form.is_valid()):

            print("passed the valid test")

            thing = thing_form.save()
            thing.category = 'Attraction'
            thing.save()

            attraction = attraction_form.save(commit=False)
            attraction.thing = thing
            attraction.save()

            pic = pic_form.save(commit=False)
            pic.thing = thing
            pic.image = request.FILES['image']
            pic.save()

            created = True
            print(created, 'created!')

        else:
            print(thing_form.errors, attraction_form.errors)
            print(pic_form.errors)

    else:
        thing_form = ThingForm()
        attraction_form = AttractionForm()
        pic_form = PictureForm()

    return render(request,
        'core/create_attraction.html',
        {
            'created': created,
            'thing_form': thing_form,
            'attraction_form': attraction_form,
            'pic_form': pic_form,})

def create_tour(request):
    created = False

    if request.method == 'POST':
        thing_form = ThingForm(data=request.POST)
        tour_form = TourForm(data=request.POST)
        pic_form = PictureForm(request.POST, request.FILES)

        print(thing_form.is_valid(), 'thing_form')
        print(tour_form.is_valid(), 'tour_form')
        print(pic_form.is_valid(), 'pic_form')

        if (thing_form.is_valid()
            and tour_form.is_valid()
            and pic_form.is_valid()):

            print("passed the valid test")

            thing = thing_form.save()
            thing.category = 'Tour'
            thing.save()

            tour = tour_form.save(commit=False)
            tour.thing = thing
            tour.save()

            pic = pic_form.save(commit=False)
            pic.thing = thing
            pic.image = request.FILES['image']
            pic.save()

            created = True
            print(created, 'created!')

        else:
            print(thing_form.errors, tour_form.errors)
            print(pic_form.errors)

    else:
        thing_form = ThingForm()
        tour_form = TourForm()
        pic_form = PictureForm()

    return render(request,
        'core/create_tour.html',
        {
            'created': created,
            'thing_form': thing_form,
            'tour_form': tour_form,
            'pic_form': pic_form,})

#############################

# TODO if this was a class I could have all these methods namespaced
def things(request):
    categories = ['Attraction', 'Tour', 'Food', 'Outdoor Activities', 'Shopping']

    querystring = get_querystring(request, categories)
    t_things = filter_(categories, querystring)
    final_things = combine(t_things)
    context = {'things': final_things} | get_params(categories, querystring)

    return render(request, 'core/things.html', context=context)

def get_querystring(request, categories):
    querystring = []
    for category in categories:
        querystring.append(
            convert_on(request.GET.get(category.lower().replace(' ', '_'))))

    return querystring

def convert_on(category):
    if category == 'on':
        return 'checked'
    return ''

def filter_(categories, querystring):
    things = []
    for category, param in zip(categories, querystring):
        if param:
            things.append(Thing.objects.filter(category=category))

    if things:
        return things

    else:
        return [Thing.objects.all()]

def combine(things):
    if things:
        final_things = things[0]
        for thing in things[1:]:
            final_things = final_things | thing

    return final_things

def get_params(categories, querystring):
    params = {}
    for category, param in zip(categories, querystring):
        params[category.lower().replace(' ', '_')] = param

    return params

#############################