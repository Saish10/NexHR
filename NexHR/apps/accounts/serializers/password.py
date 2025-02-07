"""
Password serializer module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework import serializers
from accounts.models.account import ModelUser


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for password reset.
    """

    email = serializers.EmailField()

    def validate_email(self, value):
        """
        Validate email address.
        """
        try:
            ModelUser.objects.get(email=value)
        except ModelUser.DoesNotExist as exc:
            raise serializers.ValidationError(
                "No user found with this email address."
            ) from exc
        return value


class PasswordChangeSerializer(serializers.Serializer):
    """
    Serializer for password change.
    """

    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_old_password(self, value):
        """
        Validate old password.
        """
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct.")
        return value

    def validate_new_password(self, value):
        """
        Validate new password.
        """
        # Add any custom validation logic for the new password
        if len(value) < 8:
            raise serializers.ValidationError(
                "The new password must be at least 8 characters long."
            )
        return value
