from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField
)

from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models import Q

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField() 
    # email = EmailField(label="Email Address")
    class Meta:
        model = User
        fields = ['username','password','token']

        extra_kwargs = {"password":
                            {"write_only":True}
                                }
        
    def validate(self,data):
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