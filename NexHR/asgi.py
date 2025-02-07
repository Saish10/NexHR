"""
ASGI config for NexHR project.
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

"""
ASGI config for NexHR project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NexHR.config.settings')

application = get_asgi_application()
