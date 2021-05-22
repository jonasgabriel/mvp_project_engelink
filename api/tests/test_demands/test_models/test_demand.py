from django.test import TestCase
from django.contrib.auth.models import User
from api.models.demands import *


class DemandTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Demand.objects.create(
            part_description=PartsDescription.objects.create(
                **{"name": "Braço robótico", "price": 700000.00}
            ),
            destination_address=DestinationAddress.objects.create(
                **{
                    "street_name": "Rua Hasta la vista baby",
                    "street_number": 90,
                    "postcode_number": "707070-700",
                    "city": "Niterói",
                    "state_name": "Rio de Janeiro",
                }
            ),
            contact_information=ContactInformation.objects.create(
                **{
                    "phone_1": 1998394903,
                    "phone_2": 1998340055,
                    "email": "jazz@gmail.com",
                }
            ),
            user=User.objects.create(
                **{
                    "username": "billiejean",
                    "email": "billie@gmail.com",
                    "password": "teste",
                }
            ),
            is_completed=True,
            image_status=Demand.IMAGES_PATH[True][1],
        )

    def test_check_attributes(self) -> None:
        # Parts Descriptions
        self.assertEqual(self.instance.part_description.name, "Braço robótico")
        self.assertEqual(self.instance.part_description.price, 700000.00)

        # Destination Address
        self.assertEqual(
            self.instance.destination_address.street_name, "Rua Hasta la vista baby"
        )
        self.assertEqual(self.instance.destination_address.street_number, 90)
        self.assertEqual(
            self.instance.destination_address.postcode_number, "707070-700"
        )
        self.assertEqual(self.instance.destination_address.city, "Niterói")
        self.assertEqual(self.instance.destination_address.state_name, "Rio de Janeiro")

        # Contact Information
        self.assertEqual(self.instance.contact_information.phone_1, 1998394903)
        self.assertEqual(self.instance.contact_information.phone_2, 1998340055)
        self.assertEqual(self.instance.contact_information.email, "jazz@gmail.com")

        # User
        self.assertEqual(self.instance.user.username, "billiejean")
        self.assertEqual(self.instance.user.email, "billie@gmail.com")
        self.assertEqual(self.instance.user.password, "teste")

        self.assertTrue(self.instance.is_completed)
        self.assertEqual(self.instance.image_status, self.instance.IMAGES_PATH[True][1])

    def check_instance_deleted(self) -> None:
        error = False

        try:
            Demand.objects.get(id=1)
        except Exception:
            error = True
        self.assertTrue(error, "Se o Model Demand foi deletado tem que retornar True")

    def test_delete_cascade_part_description(self) -> None:
        instance = PartsDescription.objects.get(id=1)
        instance.delete()

        self.check_instance_deleted()

    def test_delete_cascade_destination_address(self) -> None:
        instance = DestinationAddress.objects.get(id=1)
        instance.delete()

        self.check_instance_deleted()

    def test_delete_cascade_contact_information(self) -> None:
        instance = ContactInformation.objects.get(id=1)
        instance.delete()

        self.check_instance_deleted()

    def test_delete_cascade_user(self) -> None:
        instance = User.objects.get(id=1)
        instance.delete()

        self.check_instance_deleted()
