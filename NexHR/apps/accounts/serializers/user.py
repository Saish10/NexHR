"""
User serializer module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework import serializers
from accounts.models.account import ModelUser
from base.utils.mixins import FieldsMixin


class UserSerializer(FieldsMixin, serializers.ModelSerializer):
    """
    User serializer class.
    """

    class Meta:
        model = ModelUser
        fields = (
            "internal_id",
            "email",
            "first_name",
            "last_name",
            "employee_id",
            "gender",
            "date_of_birth",
            "joining_date",
            "secondary_email",
            "country",
            "state",
            "city",
            "address_1",
            "address_2",
            "zip_code",
            "is_active",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["full_name"] = instance.get_full_name()
        if "country" in self.fields:
            representation["country"] = instance.country.internal_id
        if "state" in self.fields:
            representation["state"] = instance.state.internal_id
        return representation
