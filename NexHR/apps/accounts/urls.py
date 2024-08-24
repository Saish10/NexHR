__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.urls import path
from accounts.views.login import LoginView
from accounts.views.logout import LogoutView
from accounts.views.account import UserViewSet
from accounts.views.password import PasswordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename="account")
router.register(r'', PasswordViewSet, basename="password")


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

urlpatterns += router.urls
