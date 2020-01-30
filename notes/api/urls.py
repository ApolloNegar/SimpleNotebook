from django.urls import path
from .views import PostApiView

urlpatterns = [
    path('create-post/', PostApiView.as_view())
]