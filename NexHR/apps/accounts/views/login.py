"""
Login view module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from base.utils.response_format import APIResponse
from django.contrib.auth import authenticate
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from knox.models import AuthToken
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class LoginView(APIView):
    """
    Login view module.
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="login",
        operation_description="Login a user.",
        operation_summary="Login a user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="admin@nexhr.com",
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    default="admin@123",
                ),
            },
        ),
    )
    def post(self, request):
        """
        Login a user.
        """
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request=request, email=email, password=password)
        if user:
            auth_token, token = AuthToken.objects.create(user)
            return APIResponse.success(
                data={
                    "token": token,
                    "user_id": user.internal_id,
                    "expiry": auth_token.expiry.strftime("%d-%m-%y %I:%M %p"),
                },
                message="Successfully logged in",
            )
        return APIResponse.error(message="Invalid credentials")
