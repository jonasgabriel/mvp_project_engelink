from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import demands

routers = DefaultRouter()
routers.register("demands", demands.DemandsViewSet, "demands")

urlpatterns = [
    path("", include(routers.urls)),
]
