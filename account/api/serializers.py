from generaluser.models import User as User

from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'doctor'
        ]


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
