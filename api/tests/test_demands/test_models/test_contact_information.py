from django.test import TestCase
from api.models.demands import ContactInformation


class ContactInformationTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = ContactInformation.objects.create(
            **{
                "phone_1": 1998394903,
                "phone_2": 1998340055,
                "email": "jazz@gmail.com",
            }
        )

    def test_check_attributes(self) -> None:
        self.assertEqual(self.instance.phone_1, 1998394903)
        self.assertEqual(self.instance.phone_2, 1998340055)
        self.assertEqual(self.instance.email, "jazz@gmail.com")
