from django.db import models
from api.models.demands import PartsDescription, DestinationAddress, ContactInformation
from django.contrib.auth.models import User


class Demand(models.Model):
    IMAGES_PATH = (
        (False, "demands/completion/baseline-highlight_off.svg"),
        (
            True,
            "demands/completion/baseline-check_circle_outline.svg",
        )
    )

    part_description = models.OneToOneField(
        PartsDescription,
        on_delete=models.CASCADE,
        verbose_name="Descrição da peça",
        related_name="part_description",
    )
    destination_address = models.ForeignKey(
        DestinationAddress,
        on_delete=models.CASCADE,
        verbose_name="Endereço de entrega",
        related_name="destination_address",
    )
    contact_information = models.ForeignKey(
        ContactInformation,
        on_delete=models.CASCADE,
        verbose_name="Informações de contato",
        related_name="contact_information",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        related_name="user",
    )
    is_completed = models.BooleanField(default=False, verbose_name="Demanda Finalizada")
    image_status = models.FileField(upload_to="demands/completion/")
