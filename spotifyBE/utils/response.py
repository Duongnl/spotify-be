from rest_framework.response import Response
from rest_framework import status
from http import HTTPStatus

def ApiResponse(data=None, statusCode=status.HTTP_200_OK, error=None):

    message = HTTPStatus(statusCode).phrase

    response = {
        "status": statusCode,
        "message": message,
    }

    if data is not None:
        response["data"] = data

    if error is not None:
        response["error"] = error

    return Response(response, status=statusCode)
