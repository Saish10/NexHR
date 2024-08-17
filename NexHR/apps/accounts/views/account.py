__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.viewsets import ModelViewSet
from accounts.serializers.user import UserSerializer
from accounts.models.account import ModelUser
from base.utils.response_format import APIResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserViewSet(ModelViewSet):

    lookup_field = "internal_id"
    serializer_class = UserSerializer
    search_fields = ["email", "first_name", "last_name", "employee_id"]
    filterset_fields = [
        "is_active",
    ]

    def get_queryset(self):
        user = self.request.user
        return ModelUser.objects.all().exclude(id=user.id)

    @swagger_auto_schema(
        tags=["USER MANAGEMENT"],
        operation_id="user list",
        operation_description="Retrieve a list of users.",
        operation_summary="Retrieve a list of users.",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search for users by email or employee ID.",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "is_active",
                openapi.IN_QUERY,
                description="Filter users by active status.",
                type=openapi.TYPE_BOOLEAN,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(
            page,
            many=True,
            fields=[
                "internal_id",
                "email",
                "employee_id",
                "is_active",
            ],
        )
        data = self.get_paginated_response(serializer.data)
        return APIResponse.success(
            data=data, message="User list retrieved successfully."
        )
