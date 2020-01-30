# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # on_delete argument; If user is deleted=> delete profile.!
   

    def __str__(self):
        return f'{self.user.username} Profile'
