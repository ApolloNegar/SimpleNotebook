from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from ..models import Post
from .serializers import PostCreateSerializer
from rest_framework.permissions import (
    IsAuthenticated
)


class PostApiView(APIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)

            new_data = serializer.data
            post = Post(author=self.request.user, title=new_data['title'], content=new_data['content'])
            post.save()

            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
