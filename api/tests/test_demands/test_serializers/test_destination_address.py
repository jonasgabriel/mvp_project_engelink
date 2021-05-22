from django.test import TestCase
from api.serializers.demands import DestinationAddressSerializer
from api.models.demands import DestinationAddress


class DestinationAddressSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id": 1,
            "street_name": "Rua Hasta la vista baby",
            "street_number": 90,
            "postcode_number": "707070-700",
            "city": "Niterói",
            "state_name": "Rio de Janeiro",
        }
        self.instance = DestinationAddress.objects.create(**self.data)

    def test_serializer_destination_address(self) -> None:
        serializer = DestinationAddressSerializer(self.instance)
        self.assertEquals(serializer.data, self.data)

    def test_deserializer_destination_address(self) -> None:
        data = {
            "street_name": "Rua Monteiro Lobato",
            "street_number": 911,
            "postcode_number": "707070-700",
            "city": "Niterói",
            "state_name": "Rio de Janeiro",
        }

        serializer = DestinationAddressSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
        serializer.save()
