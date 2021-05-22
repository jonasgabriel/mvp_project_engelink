from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models import demands as models_demands
from api.serializers import demands as serializer_demands


class DemandsViewSet(viewsets.ModelViewSet):
    queryset = models_demands.Demand.objects.all()
    serializer_class = serializer_demands.DemandSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            queryset = models_demands.Demand.objects.filter(
                user__id=self.request.user.id
            )
        return super().filter_queryset(queryset)
