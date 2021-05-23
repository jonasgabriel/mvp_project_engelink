from test_plus import APITestCase
from api.models.demands import *


class IntegrationsTestCase(APITestCase):
    def setUp(self) -> None:
        user = self.make_user()
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
            user=user,
            is_completed=True,
            image_status=Demand.IMAGES_PATH[True][1],
        )

        self.login(user)

    def test_list_demands(self) -> None:
        self.get_check_200("demands-list")

    def test_create_demands(self) -> None:
        self.post(
            "demands-list",
            data={
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
            },
            extra={"format": "json"},
        )
        self.assert_http_201_created(self.last_response)

    def test_delete_demands(self) -> None:
        self.delete("demands-detail", pk=1)
        self.assert_http_204_no_content(self.last_response)

    def test_get_demands(self) -> None:
        self.get("demands-detail", pk=1)
        self.assert_http_200_ok(self.last_response)

    def test_put_demands(self) -> None:
        self.put(
            "demands-detail",
            pk=1,
            data={
                "part_description": {
                    "name": "Braco robotico",
                    "price": "700530.00",
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
            },
            extra={"format": "json"},
        )

        self.assert_http_200_ok(self.last_response)

    def test_patch_demands(self) -> None:
        self.patch(
            "demands-detail",
            pk=1,
            data={
                "part_description": {
                    "name": "Braco robotico",
                    "price": "700530.00",
                },
            },
            extra={"format": "json"},
        )

        self.assert_http_200_ok(self.last_response)
