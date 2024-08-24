__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.serializers.user import UserSerializer
from accounts.models.account import ModelUser
from base.utils.response_format import APIResponse
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class UserViewSet(ModelViewSet):

    lookup_field = "internal_id"
    serializer_class = UserSerializer
    search_fields = ["email", "first_name", "last_name", "employee_id"]
    filterset_fields = [
        "is_active",
    ]

    def get_permissions(self):
        # Allow anyone to create (signup), otherwise require authentication
        if self.action == "create":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

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

    @swagger_auto_schema(
        tags=["USER MANAGEMENT"],
        operation_id="user detail",
        operation_description="Retrieve details of a user.",
        operation_summary="Retrieve details of a user.",
        manual_parameters=[
            openapi.Parameter(
                "internal_id",
                openapi.IN_PATH,
                description="The internal ID of the user.",
                type=openapi.TYPE_STRING,
                required=True,
                pattern="^[0123456789ABCDEFGHJKMNPQRSTVWXYZ]{26}$",
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return APIResponse.success(
            data=serializer.data,
            message="User details retrieved successfully.",
        )

    @swagger_auto_schema(
        tags=["USER MANAGEMENT"],
        operation_id="user update",
        operation_description="Update details of a user.",
        operation_summary="Update details of a user.",
        manual_parameters=[
            openapi.Parameter(
                "internal_id",
                openapi.IN_PATH,
                description="The internal ID of the user.",
                type=openapi.TYPE_STRING,
                required=True,
                pattern="^[0123456789ABCDEFGHJKMNPQRSTVWXYZ]{26}$",
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, format="email"
                ),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "gender": openapi.Schema(
                    type=openapi.TYPE_STRING, enum=["male", "female"]
                ),
                "date_of_birth": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="date",
                    example="24-08-2024",
                ),
                "secondary_email": openapi.Schema(
                    type=openapi.TYPE_STRING, format="email"
                ),
                "country": openapi.Schema(type=openapi.TYPE_INTEGER),
                "state": openapi.Schema(type=openapi.TYPE_INTEGER),
                "city": openapi.Schema(type=openapi.TYPE_STRING),
                "address_1": openapi.Schema(type=openapi.TYPE_STRING),
                "address_2": openapi.Schema(type=openapi.TYPE_STRING),
                "zip_code": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return APIResponse.success(
                message="User details updated successfully.",
            )
        return APIResponse.error(errors=serializer.errors)

    @swagger_auto_schema(
        tags=["USER MANAGEMENT"],
        operation_id="user partial update",
        operation_description="Partial update details of a user.",
        operation_summary="Partial update details of a user.",
        manual_parameters=[
            openapi.Parameter(
                "internal_id",
                openapi.IN_PATH,
                description="The internal ID of the user.",
                type=openapi.TYPE_STRING,
                required=True,
                pattern="^[0123456789ABCDEFGHJKMNPQRSTVWXYZ]{26}$",
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "is_active": openapi.Schema(type=openapi.TYPE_BOOLEAN),
            },
        ),
    )
    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class(
                instance, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return APIResponse.success(
                    data={},
                    message="User details updated successfully.",
                )
            return APIResponse.error(errors=serializer.errors)
        except Http404:
            return APIResponse.error(message="User not found.")

    @swagger_auto_schema(
        tags=["USER MANAGEMENT"],
        operation_id="user delete",
        operation_description="Delete a user.",
        operation_summary="Delete a user.",
        manual_parameters=[
            openapi.Parameter(
                "internal_id",
                openapi.IN_PATH,
                description="The internal ID of the user.",
                type=openapi.TYPE_STRING,
                required=True,
                pattern="^[0123456789ABCDEFGHJKMNPQRSTVWXYZ]{26}$",
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return APIResponse.success(message="User deleted successfully.")
        except Http404:
            return APIResponse.error(message="User not found.")

    @swagger_auto_schema(
        tags=["USER MANAGEMENT"],
        operation_id="user signup",
        operation_description="Signup a new user.",
        operation_summary="Signup a new user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, format="email"
                ),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING),
                "gender": openapi.Schema(
                    type=openapi.TYPE_STRING, enum=["male", "female"]
                ),
                "date_of_birth": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format="date",
                    example="24-08-2024",
                ),
                "secondary_email": openapi.Schema(
                    type=openapi.TYPE_STRING, format="email"
                ),
                "country": openapi.Schema(type=openapi.TYPE_INTEGER),
                "state": openapi.Schema(type=openapi.TYPE_INTEGER),
                "city": openapi.Schema(type=openapi.TYPE_STRING),
                "address_1": openapi.Schema(type=openapi.TYPE_STRING),
                "address_2": openapi.Schema(type=openapi.TYPE_STRING),
                "zip_code": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return APIResponse.success(
                data=serializer.data,
                message="User signed up successfully.",
                status=201,  # Created
            )
        return APIResponse.error(message=serializer.errors)
