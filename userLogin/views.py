# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


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
        form = UserRegisterForm()

    return render(request, 'userLogin/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'userLogin/profile.html')
