"""
URL configuration for NexHR project.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"


from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

SchemaView = get_schema_view(
    openapi.Info(
        title="NexHR API",
        default_version="v1",
        description="API documentation for NexHR",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("base/", include("base.urls"), name="base"),
    path("account/", include("accounts.urls"), name="account"),
]

admin.site.site_header = "NexHR Admin"
