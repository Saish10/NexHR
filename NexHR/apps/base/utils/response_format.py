# utils/response_format.py
from rest_framework.response import Response


class APIResponse:
    """
    A class for formatting API responses.
    """
    def success(data=None, message=None, status=200):
        """
        Formats the response to include data, message, and status.

        :param data: The data to be returned in the response.
        :param message: A message describing the result of the request.
        :param status: HTTP status code for the response.
        :return: A Response object formatted as specified.
        """
        response_data = {
            'data': data,
            'message': message
        }
        return Response(response_data, status=status)

    def error(message="something went wrong", status=400):
        """
        Formats the response for errors.

        :param message: A message describing the error.
        :param status: HTTP status code for the response.
        :return: A Response object formatted as specified.
        """
        response_data = {
            'data': None,
            'message': message
        }
        return Response(response_data, status=status)