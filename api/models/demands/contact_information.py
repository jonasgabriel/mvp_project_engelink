from django.db import models
from phone_field import PhoneField


class ContactInformation(models.Model):
    phone_1 = PhoneField(help_text="Número do telefone 1", verbose_name='Número do telefone 1')
    phone_2 = PhoneField(blank=True, help_text="Número do telefone 2", verbose_name='Número do telefone 2')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
