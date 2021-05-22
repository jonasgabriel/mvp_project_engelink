from django.contrib import admin
from .models import demands


@admin.register(demands.Demand)
class DemandAdmin(admin.ModelAdmin):
    exclude = ('image_status',)


@admin.register(demands.ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(demands.PartsDescription)
class PartsDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(demands.DestinationAddress)
class DestinationAddressAdmin(admin.ModelAdmin):
    pass
