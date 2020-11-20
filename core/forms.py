from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password2','password1']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        exclude=['merchant']