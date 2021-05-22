from django.test import TestCase
from api.serializers.demands import PartsDescriptionSerializer
from api.models.demands import PartsDescription


class PartDescriptionSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {"id": 1, "name": "Braço robótico", "price": 700000.00}
        self.instance = PartsDescription.objects.create(**self.data)

    def test_serializer_part_description(self) -> None:
        serializer = PartsDescriptionSerializer(self.instance)
        self.assertEquals(serializer.data, self.data)

    def test_deserializer_part_description(self) -> None:
        data = {"name": "Perna robótica", "price": 700000.00}

        serializer = PartsDescriptionSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
        serializer.save()
