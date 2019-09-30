# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest

from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'notes/user_post.html'
    context_object_name = "posts"

    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class UserPostDetailView(DetailView):
    model = Post


class UserCreateView(LoginRequiredMixin, CreateView):  # a view with a form, when we create a new post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):  # a view with a form, when we create a new post
    model = Post
    fields = ['title', 'content']
    model.date_modified = models.DateTimeField(default=timezone.now)
    print(model.date_modified)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
