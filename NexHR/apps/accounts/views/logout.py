"""
Logout view module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from base.utils.response_format import APIResponse
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class LogoutView(APIView):
    """View for logging out a user."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        tags=["AUTH"],
        operation_id="logout",
        operation_description="Logout a user.",
        operation_summary="Logout a user.",
    )
    def post(self, request):
        """
        Logout a user.
        """
        AuthToken.objects.filter(user=request.user).delete()
        return APIResponse.success(data={}, message="Successfully logged out")
