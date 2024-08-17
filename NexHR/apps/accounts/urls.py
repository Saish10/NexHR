__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.urls import path
from accounts.views.login import LoginView
from accounts.views.logout import LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
