__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.contrib import admin
from accounts.models.account import ModelUser

@admin.register(ModelUser)
class ModelUserAdmin(admin.ModelAdmin):
    list_display = ["internal_id", "email", "first_name", "last_name"]
    search_fields = ["email", "first_name", "last_name"]