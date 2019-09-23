# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest

from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Post


# Create your views here.

def notes(request):

    return render(request, 'notes/main_page.html')


class UserPost(ListView):
    model = Post
    template_name = 'notes/notes.html'
    context_object_name = 'posts'
    ordering = ['-data_posted']
