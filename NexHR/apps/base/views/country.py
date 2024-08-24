__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.viewsets import GenericViewSet
from base.utils.response_format import APIResponse
from base.models.country import ModelCountry
from base.serializers.country import CountrySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

class CountryListView(GenericViewSet):
    permission_classes = [AllowAny]
    queryset = ModelCountry.objects.all()
    serializer_class = CountrySerializer
    search_fields = ["name"]
    pagination_class = None

    @swagger_auto_schema(
        tags=["BASE"],
        operation_id="country list",
        operation_description="Retrieve a list of countries.",
        operation_summary="Retrieve a list of countries.",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search for countries by name.",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return APIResponse.success(
            data=serializer.data, message="Countries retrieved successfully"
        )
