from django.test import TestCase
from api.models.demands import PartsDescription


class PartsDescriptionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = PartsDescription.objects.create(
            **{"name": "Braço robótico", "price": 700000.00}
        )

    def test_check_attributes(self) -> None:
        self.assertEqual(self.instance.name, "Braço robótico")
        self.assertEqual(self.instance.price, 700000.00)

    def test_price_max_digits(self) -> None:
        error = False

        try:
            PartsDescription.objects.create(
                **{"name": "Perna robótica", "price": 123456789.11}
            )
        except Exception:
            error = True
        self.assertTrue(
            error,
            "Tem que retornar True se o campo price não aceitar maior que 10 digitos",
        )
