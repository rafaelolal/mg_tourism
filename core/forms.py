from django import forms
from django.contrib.auth.models import User
from core.models import UserProfileInfo, Picture

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['biography', 'profile_pic']

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image']