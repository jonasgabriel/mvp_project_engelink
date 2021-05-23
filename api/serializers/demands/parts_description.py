from rest_framework import serializers
from api.models import demands


class PartsDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = demands.PartsDescription
        fields = "__all__"
