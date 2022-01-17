"""Forms used by models that do not have a CreateView or UpdateView
All forms use the crispy_forms django app, including the ones in CreateViews or UpdateViews
crispy_forms: https://django-crispy-forms.readthedocs.io/en/latest/
"""

from django import forms
from core.models import UserProfile, Picture

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'biography', 'profile_pic']

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image']