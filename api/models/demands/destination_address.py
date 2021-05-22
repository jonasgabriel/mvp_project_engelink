from django.db import models


class DestinationAddress(models.Model):
    street_name = models.CharField(max_length=100, verbose_name="Nome da Rua")
    street_number = models.IntegerField(verbose_name="Número da Rua")
    postcode_number = models.CharField(max_length=10, verbose_name="Cep")
    city = models.CharField(max_length=100, verbose_name="Cidade")
    state_name = models.CharField(max_length=20, verbose_name="Nome do Estado")
