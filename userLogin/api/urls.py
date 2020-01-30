from django.urls import path
from django.contrib import admin

from .views import (
    UserLoginApiView,
    UserCreateApiView
)

urlpatterns = [
    path('login/',UserLoginApiView.as_view()),
    path('register/',UserCreateApiView.as_view())
    
]
