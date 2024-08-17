__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

class APIResponse:
    """
    A class for formatting API responses.
    """

    @staticmethod
    def success(data=None, message=None, status=HTTP_200_OK):
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


    @staticmethod
    def error(message="something went wrong", status=HTTP_400_BAD_REQUEST):
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