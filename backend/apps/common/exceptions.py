from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.exceptions import APIException

# Base API Exception 
class BaseAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "A server error occurred."
    default_code = "error"

class BadRequest(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Bad request."
    default_code = "bad_request"

class Unauthorized(BaseAPIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Authentication required."
    default_code = "unauthorized"


class Forbidden(BaseAPIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "You do not have permission to perform this action."
    default_code = "forbidden"


class NotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Resource not found."
    default_code = "not_found"


class Conflict(BaseAPIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Conflict occurred."
    default_code = "conflict"


class ServerError(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Internal server error."
    default_code = "server_error"


# Custom DRF Exception Handler
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    request = context.get("request")

    # Known DRF exceptions
    if response is not None:
        return Response(
            {
                "success": False,
                "status_code": response.status_code,
                "message": "Request failed",
                "timestamp": timezone.now(),
                "path": request.path if request else None,
                "errors": response.data,
            },
            status=response.status_code,
        )

    # Unhandled exceptions (bugs, crashes, etc.)
    return Response(
        {
            "success": False,
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "Internal server error",
            "timestamp": timezone.now(),
            "path": request.path if request else None,
            "errors": "Unexpected error occurred.",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

