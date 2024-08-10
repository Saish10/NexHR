__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.contrib import admin
from base.models.country import ModelCountry
from base.models.state import ModelState


@admin.register(ModelCountry)
class ModelCountryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "isd_code",
        "alpha3_code",
        "currency_alpha3",
    ]
    search_fields = ["name", "alpha2_code", "alpha3_code", "isd_code"]


@admin.register(ModelState)
class ModelStateAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "country"]
    search_fields = ["name", "code", "country__name"]
