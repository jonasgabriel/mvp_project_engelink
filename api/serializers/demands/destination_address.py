from rest_framework import serializers
from api.models import demands


class DestinationAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = demands.DestinationAddress
        fields = "__all__"
