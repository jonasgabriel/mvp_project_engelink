from django.test import TestCase
from api.serializers.demands import ContactInformationSerializer
from api.models.demands import ContactInformation


class ContactInformationSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id": 1,
            "phone_1": "1998394903",
            "phone_2": "1998340055",
            "email": "jazz@gmail.com",
        }
        self.instance = ContactInformation.objects.create(**self.data)

    def test_serializer_contact_information(self) -> None:
        serializer = ContactInformationSerializer(self.instance)
        self.assertEquals(serializer.data, self.data)

    def test_deserializer_contact_information(self) -> None:
        data = {
            "phone_1": "1998394102",
            "phone_2": "1998340103",
            "email": "best@gmail.com",
        }

        serializer = ContactInformationSerializer(data=data)
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
        serializer.save()
