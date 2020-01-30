from rest_framework.serializers import (

    CharField,
    ModelSerializer,
    ValidationError,

)

from django.contrib.auth import get_user_model
from rest_framework.generics import (
        CreateAPIView
)
from django.db.models import Q

User = get_user_model()

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    
    class Meta:
        model = User
        fields = ['username', 'password', 'token']

        extra_kwargs = {"password": {"write_only": True} }

    def validate(self, data):
        user_obj = None
        username = data.get("username")
        password = data.get("password")
        if not username:
            raise ValidationError("Enter your username!")

        user = User.objects.filter(Q(username=username))

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username is not valid!")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password!")
        data["token"] = "some random token"
        return data

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password'
        ]

        extra_kwargs = { 
            "password":
                {"write_only":True}
                        }
        
        # overriding create()
    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data