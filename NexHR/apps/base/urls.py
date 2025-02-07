"""
Base urls module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from base.views.country import CountryListView
from base.views.state import StateListView


router = DefaultRouter()
router.register(r"countries", CountryListView, basename="country")
router.register(r"states", StateListView, basename="state")

urlpatterns = [
    path("", include(router.urls)),
]
