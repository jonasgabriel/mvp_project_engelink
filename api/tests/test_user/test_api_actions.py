from test_plus import APITestCase


class IntegrationsTestCase(APITestCase):
    def setUp(self) -> None:
        self.make_user(username="jonas", password="jonas10")

    def test_login(self) -> None:
        self.post(
            "login",
            data={"username": "jonas", "password": "jonas10"},
            extra={"format": "json"},
        )

        self.assert_http_200_ok(self.last_response)
