from rest_framework import serializers
from base.models.state import ModelState

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelState
        fields = ['internal_id', 'name', 'code']