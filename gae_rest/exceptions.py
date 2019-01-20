from gae_rest import status


class ErrorDetail(object):
    def __init__(self, message, code):
        self.message = message
        self.code = code


def _get_error_detail(data, default_code=None):
    """
    A recursive function to make eventual message string to ErrorDetail object
    """
    if isinstance(data, list):
        return [_get_error_detail(msg, default_code) for msg in data]
    elif isinstance(data, dict):
        return {key: _get_error_detail(value, default_code) for key, value in data.items()}

    return ErrorDetail(data, default_code)


class APIException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_message = ("internal server error",)
    default_code = "internal_server_error"

    def __init__(self, message=None, code=None):
        if message is None:
            message = self.default_message
        if code is None:
            code = self.default_code

        self.message = message
        self.code = code

        if not isinstance(message, dict) or not isinstance(message, list):
            self.detail = [message]

        self.detail = _get_error_detail(self.message, self.code)


class ValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_message = ("value is not valid", )
    default_code = "not_valid"


"""
Usage:
    `raise ValidationError(message="only unique strings", code="value_not_valid")`

def validate_not_none(value):
    if value is None:
        raise ValidationError("value can not be None")

try:
    validate_not_none(None)
except ValidationError as eobj:
    print(eobj)

"""

