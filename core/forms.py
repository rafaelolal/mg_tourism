from django import forms
from django.contrib.auth.models import User
from core.models import UserProfileInfo, Thing, Attraction, Tour, Picture

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['profile_pic']

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ['stars', 'category']

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        exclude = ['thing']

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        exclude = ['thing']

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image']