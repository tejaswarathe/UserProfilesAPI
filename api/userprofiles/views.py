from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import (
    UserListSerializer,
    UserDetailSerializer, 
    UserCreateSerializer
)


# Create your views here.
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'name'

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer