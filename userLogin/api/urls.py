from django.conf.urls import url 
from django.contrib import admin

from .views import (
    UserLoginApiView
)


urlpatterns = [
    url(r'^login/', UserLoginApiView.as_view(), name='login')
]