from rest_framework.serializers import (
    ModelSerializer
)
from ..models import Post
from rest_framework.serializers import (
    CharField
)
from django.contrib.auth import get_user_model

User = get_user_model()


class PostCreateSerializer(ModelSerializer):
    id = CharField(read_only=True)
    title = CharField()
    content = CharField()
    author = CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author']

    def validate(self, data):
        content = data.get("content")
        title = data.get("title")

        return data
