# from django.conf import settings  # evabe likhle django te custom user nibe na
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    ValidationError,
    HyperlinkedIdentityField,
)
User = get_user_model()

# User = settings.AUTH_USER_MODEL # evabe likhle django te custom user nibe na


class UserCreationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'doctor'
        ]
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            print('ami ekhane achi\n')
            print(validated_data)
            print('amar kaj shesh\n')
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            user_obj = User(
                email=email,
                username=username,
            )
            user_obj.set_password(password)
            user_obj.save()
            print(user_obj)
            return validated_data


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def validate(self, data):
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password')
        if not username and not email:
            raise ValidationError('Username or email are required for login!')
        user = User.objects.filter(
            Q(username=username) |
            Q(email=email)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_data = user.first()
        else:
            raise ValidationError('Username or Email is not valid!')
        if user_data:
            if not user_data.check_password(password):
                raise ValidationError('Incorrect Password!')
        return data
