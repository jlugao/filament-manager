from django.contrib import admin
from .models import Filament, Manufacturer

# Register your models here.


@admin.register(Filament)
class FilamentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "uuid",
        "brand",
        "material",
        "type",
        "price",
        "quantity_in_kg",
        "description",
        "url",
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name",)
