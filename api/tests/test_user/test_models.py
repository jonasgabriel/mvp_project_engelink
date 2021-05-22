from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = User.objects.create(
            **{
                "username": "billieJean",
                "email": "billie@gmail.com",
                "password": "teste",
            }
        )

    def test_check_attributes(self) -> None:
        self.assertEqual(self.instance.username, "billieJean")
        self.assertEqual(self.instance.email, "billie@gmail.com")
        self.assertEqual(self.instance.password, "teste")
