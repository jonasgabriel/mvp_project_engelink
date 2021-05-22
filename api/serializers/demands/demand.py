from rest_framework import serializers
from api.models import demands
from .parts_description import PartsDescriptionSerializer
from .contact_information import ContactInformationSerializer
from .destination_address import DestinationAddressSerializer
from api.serializers.user import UserSerializer
from api.models.demands import *
from django.contrib.auth.models import User


class DemandSerializer(serializers.ModelSerializer):
    part_description = PartsDescriptionSerializer()
    destination_address = DestinationAddressSerializer()
    contact_information = ContactInformationSerializer()
    user = UserSerializer(read_only=True)

    class Meta:
        model = demands.Demand
        fields = "__all__"
        extra_kwargs = {"image_status": {"read_only": True}}

    def create(self, validated_data):
        user = None

        if "test_user" in self.context:
            user = self.context["test_user"]

        if "request" in self.context:
            user = self.context["request"].user

        if (
            "part_description" in validated_data
            and "destination_address" in validated_data
            and "contact_information" in validated_data
            and "is_completed" in validated_data
            and user is not None
        ):
            # Parts description
            part_instance = PartsDescription(**validated_data["part_description"])
            part_instance.save()

            # Destination address
            address_instance = DestinationAddress(
                **validated_data["destination_address"]
            )
            address_instance.save()

            # Contact information
            contact_instance = ContactInformation(
                **validated_data["contact_information"]
            )
            contact_instance.save()

            instance_user = User.objects.get(id=user.id)

            try:
                demand_instance = Demand(
                    part_description=part_instance,
                    destination_address=address_instance,
                    contact_information=contact_instance,
                    user=instance_user,
                    is_completed=validated_data["is_completed"],
                    image_status=Demand.IMAGES_PATH[validated_data["is_completed"]][1],
                )

                demand_instance.save()
            except Exception:
                raise Exception
            return demand_instance
        return None

    def update(self, instance, validated_data):
        if "part_description" in validated_data:
            for attr, value in validated_data["part_description"].items():
                setattr(instance.part_description, attr, value)
            instance.part_description.save()
        if "destination_address" in validated_data:
            for attr, value in validated_data["destination_address"].items():
                setattr(instance.destination_address, attr, value)
            instance.destination_address.save()

        if "contact_information" in validated_data:
            for attr, value in validated_data["contact_information"].items():
                setattr(instance.contact_information, attr, value)
            instance.contact_information.save()

        if "is_completed" in validated_data:
            instance.is_completed = validated_data["is_completed"]
            instance.image_status = instance.IMAGES_PATH[
                validated_data["is_completed"]
            ][1]
            instance.save()

        return instance
