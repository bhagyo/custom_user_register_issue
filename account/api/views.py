from django.shortcuts import render
"""
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.db.models import Q
from rest_framework.mixins import DerstroyModelMixin, UpdateModelMixin
from rest_framework.serializers import(
    ValidationError
)

"""
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)


from rest_framework.permissions import(
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework import generics
from .serializers import UserCreationSerializer, UserListSerializer, LoginSerializer


from django.contrib.auth import get_user_model
User = get_user_model()


class UserListSingleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all().order_by('-id')[:1]
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny, ]


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    #permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
