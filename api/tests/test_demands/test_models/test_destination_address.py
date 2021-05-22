from django.test import TestCase
from api.models.demands import DestinationAddress


class DestinationAddressTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = DestinationAddress.objects.create(
            **{
                "street_name": "Rua Hasta la vista baby",
                "street_number": 90,
                "postcode_number": "707070-700",
                "city": "Niterói",
                "state_name": "Rio de Janeiro",
            }
        )

    def test_check_attributes(self) -> None:
        self.assertEqual(self.instance.street_name, "Rua Hasta la vista baby")
        self.assertEqual(self.instance.street_number, 90)
        self.assertEqual(self.instance.postcode_number, "707070-700")
        self.assertEqual(self.instance.city, "Niterói")
        self.assertEqual(self.instance.state_name, "Rio de Janeiro")
