from django.shortcuts import render

from rest_framework import generics

from .serializers import UserCreationSerializer, UserListSerializer

from generaluser.models import User as User


class UserListSingleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')[:1]
    serializer_class = UserCreationSerializer
