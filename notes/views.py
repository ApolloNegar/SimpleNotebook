# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest
from .models import Note
from django.shortcuts import render, redirect


# Create your views here.

def notes(request):
    return render(request, 'notes/notes.html')
