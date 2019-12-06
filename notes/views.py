# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest

from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)

from .models import Post


# Create your views here.


def notes(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'notes/notes.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = 'notes/table_notes.html'  # ex: user_post.html
    context_object_name = "posts"

    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # print(self.request.POST.get('order'))
        return Post.objects.filter(author=user).order_by('order')


class UserPostDetailView(DetailView):
    model = Post


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):  # a view with a form, when we update a post
    model = Post
    fields = ['title', 'content']

    success_url = '/user-direct/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        now = timezone.now()
        form.instance.date_modified = now
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/reorder/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


def user_direct(request):
    return redirect('user-posts', request.user.username)


@login_required
def post_order_change(request, **order):
    if request.method == 'POST':
        # try:

        o = request.POST.get('order')  # goal order

        p_1 = Post.objects.get(author=request.user, order=order['order'])  # the current order of the post
        p_2 = Post.objects.get(author=request.user, order=int(o))  # target post

        p_2.order = int(order['order'])
        p_2.save()
        p_1.order = int(o)

        p_1.save()

    else:
        pass
    context = {'user': request.user}
    return render(request, 'notes/post_order.html', context)


def reorder(request, ):
    total_count = Post.objects.filter(author=request.user).count()

    t = total_count
    while 0 < t:
        for p in Post.objects.filter(author=request.user):
            p.order = t
            p.save()
            t -= 1

    return redirect('/user/{}'.format(request.user))


class UserCreateView(LoginRequiredMixin, CreateView):  # a view with a form, when we create a new post
    model = Post
    fields = ['title', 'content']

    success_url = '/user-direct/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        total_count = Post.objects.filter(author=self.request.user).count()
        print(total_count)
        t = total_count
        if t == 1:
            form.instance.order = 1
        else:
            while 1 < t:
                for p in Post.objects.filter(author=self.request.user):
                    p.order = t
                    p.save()
                    t -= 1

            form.instance.order = 1

        return super().form_valid(form)
