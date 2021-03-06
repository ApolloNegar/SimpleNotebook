"""SimpleNotebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views as auth_views
from notes.views import (
        UserPostDetailView, 
        UserCreateView, 
        UserUpdateView, 
        UserDeleteView,
        UserPostListView,
        user_direct,
        post_order_change,
        reorder)
from userLogin.views import register
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='userLogin/login.html'), name='main-page'),

    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='userLogin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userLogin/logout.html'), name='logout'),

    
    path('post/<int:pk>/', UserPostDetailView.as_view(), name="post-detail"),
    path('new-post/', UserCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', UserUpdateView.as_view(), name="post-update"),

    path('post/<int:order>', post_order_change, name="post-order"),
    path('reorder/', reorder, name='post-reorder'),

    path('post/<int:pk>/delete', UserDeleteView.as_view(), name="post-delete"),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user-direct/', user_direct, name="user-direct"),
    
    # api_urls
    path('api/posts/', include('notes.api.urls', namespace=None), name='post-api'),
    path('api/users/', include('userLogin.api.urls', namespace=None),name='user-api')
    

]
