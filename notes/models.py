# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Note(models.Model):
    priority = models.IntegerField(max_length=10)
    title = models.CharField(max_length=100)
    date_of_creation = models.DateTimeField(auto_created=True)
    text = models.TextField(max_length=1000000)
    last_edit = models.DateTimeField(auto_created=True)
