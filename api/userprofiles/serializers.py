from rest_framework import serializers
from stdimage_serializer.fields import StdImageField



from .models import User

class UserListSerializer(serializers.ModelSerializer):
    picture = StdImageField()

    class Meta:
        model = User
        fields = ('name', 'picture')

class UserDetailSerializer(serializers.ModelSerializer):
    picture = StdImageField()

    class Meta:
        model = User
        fields = ('name', 'picture', 'timestamp')


class UserCreateSerializer(serializers.ModelSerializer):
    picture = StdImageField()

    class Meta:
        model = User
        fields = ('name', 'picture')
