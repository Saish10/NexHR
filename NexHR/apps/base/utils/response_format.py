__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


class APIResponse:
    """
    A class for formatting API responses.
    """

    @staticmethod
    def success(data, message=None, status=HTTP_200_OK):
        """
        Formats the response to include data, message, and status.

        :param data: The data to be returned in the response.
        :param message: A message describing the result of the request.
        :param status: HTTP status code for the response.
        :return: A Response object formatted as specified.
        """
        # Create a dictionary to store the response data
        response_data = {"data": data, "message": message}
        # Return the response object
        return Response(response_data, status=status)

    @staticmethod
    def error(
        message="Something went wrong.",
        errors=None,
        status=HTTP_400_BAD_REQUEST,
    ):
        """
        Formats the response for errors.

        :param message: A message describing the error.
        :param errors: A dictionary of errors.
        :param status: HTTP status code for the response.
        :return: A Response object formatted as specified.
        """
        # If there are errors, convert them to a string
        if errors:
            message = serialize_error_message(errors)
        # Create the response data
        response_data = {"data": None, "message": message}
        # Return the response
        return Response(response_data, status=status)



def serialize_error_message(errors):
    """
    Converts a dictionary of field errors into a formatted string.

    The string is formatted as: "Field Name, Error Message". If the error is a
    non-field error, the string is formatted as: "Error Message".

    :param errors: A dictionary of field errors.
    :return: A formatted string of the error messages.
    """
    # Get the first error
    error = list(errors)[0]
    # Get the error message
    str_msg = errors[error][0]
    # Create the message, if the error is a non-field error, don't add the field name
    msg = (
        ""
        if error == "non_field_errors"
        else error.capitalize().replace("_", " ") + ", "
    )
    # Add the error message to the message
    msg = msg + str_msg
    # Return the formatted message
    return msg
