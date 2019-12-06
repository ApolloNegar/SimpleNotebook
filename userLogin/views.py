# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView
# from django.contrib.auth.views
from .forms import UserRegisterForm, UserLoginForm, Verification
import re
import socket
import time
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


def email_check(request):
    email_check.counter += 1

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + ip)

        if form.is_valid():
            e = request.POST.get('email')
            t = User.objects.filter(email=e)
            print(email_check.counter)
            if email_check.counter < 6:
                if t:
                    return redirect('login')
                else:
                    return redirect('email-check')
            else:

                return render(request, 'userLogin/blocked_ip.html')

        else:
            return HttpResponse('')
    else:
        form = UserLoginForm()
    return render(request, 'userLogin/phone_input.html', {'form': form})


email_check.counter = 0


def code_check(request, **verify):
    if request.method == 'POST':
        user_input = request.POST.get('user_code_input')
        # print(type(user_input), type(verify['verify']))
        if int(user_input) == verify['verify']:
            return redirect('register')
        else:
            return redirect('email-check')
    else:
        pass


def verification_code(request, **verify):
    code = randrange(10000, 100000)
    if request.method == 'POST':
        form = Verification(request.POST)
        if form.is_valid():
            c = request.POST.get('user_code_input')
            # print('user input:', c)
            # print('code generated:', code)
            # print('code on page:', verify, 20000000000000000000000)
            if c == verify:
                print('yes!')
        else:
            pass
    else:
        form = Verification()
        print(code, 'second')

    return render(request, 'userLogin/verification_code.html', {'form': form, 'verify': code})
