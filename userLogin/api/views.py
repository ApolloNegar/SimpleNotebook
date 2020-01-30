from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from .serializers import UserLoginSerializer, UserCreateSerializer

User = get_user_model()


class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        
        data = request.data
        serilizer = UserLoginSerializer(data=data)
        if serilizer.is_valid(raise_exception=True):
            new_data = serilizer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serilizer.errors, status=HTTP_400_BAD_REQUEST)

class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer