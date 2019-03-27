from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .serializers import UserListSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(name=""):
        if name != "":
            User.objects.create(name=name)

    def setUp(self):
        # add test data
        self.create_user("Jeff")
        self.create_user("Betty")


class GetAllUsersTest(BaseViewTest):

    def test_get_all_songs(self):

        # hit the API endpoint
        response = self.client.get(
            reverse("userlist")
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UserListSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)