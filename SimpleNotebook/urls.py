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

from django.urls import path
from django.contrib import admin

from django.contrib.auth import views as auth_views
from notes.views import UserPost, notes
from userLogin import views as user_views

urlpatterns = [
    path('', notes, name='main-page'),
    path('posts', UserPost.as_view(), name="blog-home"),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userLogin/login.html'), name='login'),
    # telling django where to look for template
    path('logout/', auth_views.LogoutView.as_view(template_name='userLogin/logout.html'), name='logout'),
    path('admin/', admin.site.urls),

]
