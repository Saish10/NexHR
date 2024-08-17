__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.urls import path
from base.views.country import CountryListView
from base.views.state import StateListView


urlpatterns = [
    path("countries/", CountryListView.as_view(), name="country_list"),
    path(
        "states/<str:country_id>/", StateListView.as_view(), name="state_list"
    ),
]
