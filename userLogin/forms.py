from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from random import randrange


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=120, label='email')


