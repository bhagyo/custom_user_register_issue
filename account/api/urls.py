# api er url
from django.urls import path

from .views import UserCreateAPIView, UserListSingleAPIView, UserListAPIView, LoginAPIView

urlpatterns = [
    path('user/<int:pk>/', UserListSingleAPIView.as_view(), name='user_single'),
    path('user/', UserListAPIView.as_view(), name='user'),
    path('register/', UserCreateAPIView.as_view(), name='user_register'),
    path('login/', LoginAPIView.as_view(), name='user_login'),

]
