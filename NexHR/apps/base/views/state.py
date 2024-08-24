__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.viewsets import GenericViewSet
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from base.models.state import ModelState
from base.serializers.state import StateSerializer
from base.utils.response_format import APIResponse
from rest_framework.permissions import AllowAny


class StateListView(GenericViewSet):
    lookup_field = "country_id"
    permission_classes = [AllowAny]
    serializer_class = StateSerializer
    search_fields = ["name"]

    def get_queryset(self):
        country_id = self.kwargs['country_id']  # Capture the path parameter
        if country_id:
            return ModelState.objects.filter(country__internal_id=country_id)
        return ModelState.objects.all()

    @swagger_auto_schema(
        tags=["BASE"],
        operation_id="state list",
        operation_description="Retrieve a list of states.",
        operation_summary="Retrieve a list of states.",
        manual_parameters=[
            openapi.Parameter(
                "country_id",
                openapi.IN_PATH,
                description="Filter states by country ID.",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search for states by name.",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return APIResponse.success(
            data=serializer.data, message="States retrieved successfully"
        )
