from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    UserCreateView
)


urlpatterns = [
    path('users/', UserListView.as_view(), name='userlist'),
    path('users/<str:name>', UserDetailView.as_view(), name='userdetail'),
    path('users/create/', UserCreateView.as_view(), name='usercreate'),
]