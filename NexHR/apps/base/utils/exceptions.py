__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.views import exception_handler
from .response_format import APIResponse
from rest_framework.exceptions import APIException, ValidationError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    # If response is None, this is an unhandled exception
    if response is None:
        return APIResponse.error(
            message="An unexpected error occurred.", status=500
        )

    # For ValidationError and other APIExceptions
    if isinstance(exc, ValidationError):
        message = (
            exc.detail if isinstance(exc.detail, str) else " ".join(exc.detail)
        )
        return APIResponse.error(message=message, status=400)

    if isinstance(exc, APIException):
        message = (
            exc.detail if isinstance(exc.detail, str) else " ".join(exc.detail)
        )
        return APIResponse.error(message=message, status=response.status_code)

    # If it's not an APIException, just return the response as is
    return APIResponse.error(message=str(exc), status=response.status_code)
