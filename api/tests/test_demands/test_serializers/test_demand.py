from django.test import TestCase
from api.serializers.demands import *
from api.models.demands import *
from django.contrib.auth.models import User
from collections import OrderedDict


class DemandSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id": 1,
            "part_description": OrderedDict(
                [("id", 1), ("name", "Braco robotico"), ("price", 700000.00)]
            ),
            "destination_address": OrderedDict(
                [
                    ("id", 1),
                    ("street_name", "Rua Hasta la vista baby"),
                    ("street_number", 90),
                    ("postcode_number", "707070-700"),
                    ("city", "Niterói"),
                    ("state_name", "Rio de Janeiro"),
                ]
            ),
            "contact_information": OrderedDict(
                [
                    ("id", 1),
                    ("phone_1", "1998394903"),
                    ("phone_2", "1998340055"),
                    ("email", "jazz@gmail.com"),
                ]
            ),
            "user": OrderedDict([("id", 1), ("username", "billieJean")]),
            "is_completed": True,
            "image_status": "/media/demands/completion/baseline-check_circle_outline.svg",
        }

        self.instance = Demand.objects.create(
            part_description=PartsDescription.objects.create(
                **self.data["part_description"]
            ),
            destination_address=DestinationAddress.objects.create(
                **self.data["destination_address"]
            ),
            contact_information=ContactInformation.objects.create(
                **self.data["contact_information"]
            ),
            user=User.objects.create(
                **{
                    "username": "billieJean",
                    "email": "billie@gmail.com",
                    "password": "teste",
                }
            ),
            is_completed=True,
            image_status=Demand.IMAGES_PATH[True][1],
        )

    def test_serializer_demand(self) -> None:
        serializer = DemandSerializer(self.instance)
        self.assertEquals(serializer.data, self.data)

    def test_deserializer_demands(self) -> None:
        data = {
            "part_description": {
                "name": "Braco robotico",
                "price": "700000.00",
            },
            "destination_address": {
                "street_name": "Rua Hasta la vista baby",
                "street_number": 90,
                "postcode_number": "707070-700",
                "city": "Niterói",
                "state_name": "Rio de Janeiro",
            },
            "contact_information": {
                "phone_1": "1998394903",
                "phone_2": "1998340055",
                "email": "jazz@gmail.com",
            },
            "is_completed": True,
            "image_status": "/media/demands/completion/baseline-check_circle_outline.svg",
        }

        serializer = DemandSerializer(
            data=data,
            context={
                "test_user": User.objects.create(
                    **{
                        "username": "michael",
                        "email": "michael@gmail.com",
                        "password": "teste",
                    }
                )
            },
        )
        is_valid = serializer.is_valid()
        self.assertTrue(is_valid)
        serializer.save()
