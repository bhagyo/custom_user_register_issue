# from django.conf import settings  # evabe likhle django te custom user nibe na
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    Serializer,
    ValidationError,
    HyperlinkedIdentityField,
)
User = get_user_model()

# User = settings.AUTH_USER_MODEL # evabe likhle django te custom user nibe na


class UserCreationSerializer(ModelSerializer):
    password_confirmation = CharField(label='Confirm Password')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_confirmation',
            'doctor'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, username):
        #username = data['username']
        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("This username is used")
        return username

    def validate_email(self, email):
        #email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This email is used")
        return email

    def validate_password_confirmation(self, password_confirmation):
        data = self.get_initial()
        password = data.get('password')
        password_confirmation = password_confirmation
        if password != password_confirmation:
            raise ValidationError('Passwords dose not matched!')
        return password_confirmation

    def create(self, validated_data):
        print('ami ekhane achi\n')
        print(validated_data)
        print('amar kaj shesh\n')
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        doctor = validated_data['doctor']
        user_obj = User(
            email=email,
            username=username,
            doctor=doctor,
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
