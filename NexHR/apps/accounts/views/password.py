"""
Password view module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from accounts.serializers.password import (
    PasswordChangeSerializer,
    PasswordResetSerializer,
)
from base.utils.response_format import APIResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PasswordViewSet(GenericViewSet):
    """ViewSet for password operations."""

    def get_permissions(self):
        if self.action == "change":
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="forgot password",
        operation_description="Request a password reset link.",
        operation_summary="Forgot password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, format="email"
                ),
            },
            required=["email"],
        ),
    )
    @action(detail=False, methods=["post"], url_path="forgot-password")
    def forgot(self, request):
        """
        Request a password reset link.
        """
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            # Assuming you have a method to send the reset email
            user.send_password_reset_email()
            return APIResponse.success(
                data={},
                message="Password reset link sent successfully.",
                status=status.HTTP_200_OK,
            )
        return APIResponse.error(
            message=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="reset password",
        operation_description="Reset the password using the token sent in the email.",
        operation_summary="Reset password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "uid": openapi.Schema(type=openapi.TYPE_STRING),
                "token": openapi.Schema(type=openapi.TYPE_STRING),
                "new_password": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["uid", "token", "new_password"],
        ),
    )
    @action(detail=False, methods=["post"], url_path="reset-password")
    def reset(self, request, *args, **kwargs):
        """
        Reset the password using the token sent in the email.
        """

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="change password",
        operation_description="Change the password for the user.",
        operation_summary="Change password",
        request_body=PasswordChangeSerializer,
    )
    @action(detail=False, methods=["post"], url_path="change-password")
    def change(self, request):
        """
        Change the password for the user.
        """
        serializer = PasswordChangeSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return APIResponse.success(
                data={}, message="Password changed successfully."
            )
        return APIResponse.error(errors=serializer.errors)
