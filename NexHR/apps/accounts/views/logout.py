from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from base.utils.response_format import APIResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="logout",
        operation_description="Logout a user.",
        operation_summary="Logout a user.",
    )
    def post(self, request, *args, **kwargs):
        AuthToken.objects.filter(user=request.user).delete()
        return APIResponse.success(message="Successfully logged out")
