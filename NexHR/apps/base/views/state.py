# views.py
from rest_framework.generics import ListAPIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from base.models.state import ModelState
from base.serializers.state import StateSerializer
from base.utils.response_format import APIResponse


class StateListView(ListAPIView):
    queryset = ModelState.objects.all()
    serializer_class = StateSerializer
    search_fields = ["name"]

    def get_queryset(self):
        country_id = self.kwargs['country_id']  # Capture the path parameter
        return ModelState.objects.filter(country__internal_id=country_id)

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
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Use the filtered queryset
        serializer = self.get_serializer(queryset, many=True)
        return APIResponse.success(
            data=serializer.data, message="States retrieved successfully"
        )
