# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, UserLoginForm
from django import forms
from random import randrange


# Create your views here.




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # the validated data will be in cleaned_data!
            messages.success(request, f'Account created for {username} !')  # now update your template...
            return redirect('main-page')  # name of the url pattern
        else:
            return HttpResponse('register')
    else:
        form = UserRegisterForm()

    return render(request, 'userLogin/register.html', {'form': form})
