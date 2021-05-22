from django.test import TestCase
from api.serializers.user import UserSerializer
from django.contrib.auth.models import User


class UserSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id": 1,
            "username": "billieJean",
            "email": "billie@gmail.com",
            "password": "teste",
        }
        self.instance = User.objects.create(**self.data)

    def test_serializer_user(self) -> None:
        serializer = UserSerializer(self.instance)
        self.assertEquals(serializer.data, {"id": 1, "username": "billieJean"})

    def test_deserializer_user(self) -> None:
        data = {
            "username": "jazz",
            "email": "jazz@gmail.com",
            "password": "teste",
        }

        serializer = UserSerializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        self.assertTrue(is_valid)
        serializer.save()
