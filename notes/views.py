# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest

from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, CreateView)

from .models import Post


# Create your views here.


def notes(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'notes/notes.html', context)


class UserPost(ListView):
    model = Post
    template_name = 'notes/notes.html'
    context_object_name = "posts"
    ordering = ['-date_posted']


class UserPostDetailView(DetailView):
    model = Post


class UserCreateView(CreateView):  # a view with a form, when we create a new post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
