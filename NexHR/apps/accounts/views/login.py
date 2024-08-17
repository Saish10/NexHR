from rest_framework.views import APIView
from knox.models import AuthToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from base.utils.response_format import APIResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LoginView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="login",
        operation_description="Login a user.",
        operation_summary="Login a user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request=request, email=email, password=password)
        if user:
            auth_token, token = AuthToken.objects.create(user)
            return APIResponse.success(
                data={
                    "token": token,
                    "user_id": user.internal_id,
                    "expiry": auth_token.expiry.strftime('%d-%m-%y %I:%M %p')
                },
                message="Successfully logged in",
            )
        return APIResponse.error(message="Invalid credentials")
