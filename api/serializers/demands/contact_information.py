from rest_framework import serializers
from api.models import demands


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = demands.ContactInformation
        fields = "__all__"
