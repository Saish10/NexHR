"""
Country serializer module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework import serializers
from base.models.country import ModelCountry


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for Country model.
    """

    class Meta:
        """Class Meta"""

        model = ModelCountry
        fields = [
            "internal_id",
            "name",
            "alpha2_code",
            "alpha3_code",
            "numeric_code",
            "isd_code",
            "currency_name",
            "currency_alpha3",
            "currency_symbol",
        ]
