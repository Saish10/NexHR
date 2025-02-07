"""
State serializer module.
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework import serializers
from base.models.state import ModelState

class StateSerializer(serializers.ModelSerializer):
    """
    Serializer for State model.
    """
    class Meta:
        """Class Meta"""
        model = ModelState
        fields = ['internal_id', 'name', 'code']