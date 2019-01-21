# api er url
from django.urls import path

from .views import UserCreateAPIView, UserListSingleAPIView, UserListAPIView

urlpatterns = [
    path('user/<int:pk>/', UserListSingleAPIView.as_view()),
    path('user/', UserListAPIView.as_view()),
    path('register/', UserCreateAPIView.as_view()),

]
