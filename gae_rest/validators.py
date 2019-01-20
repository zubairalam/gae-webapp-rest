from gae_rest.exceptions import ValidationError


class MinLengthValidator(object):
    message = "Ensure value maintains minimum length required"
    code = "min_length_required"

    def __init__(self, min_length, message=None):
        self.min_length = min_length
        if message is None:
            message = self.message
        self.message = message

    def __call__(self, value):
        if not (len(value) >= self.min_length):
            raise ValidationError(self.message, self.code)


class MaxLengthValidator(object):
    message = "Ensure value doesn't exceed maximum length required"
    code = "max_length_required"

    def __init__(self, max_length, message=None):
        self.max_length = max_length
        if message is None:
            message = self.message
        self.message = message

    def __call__(self, value):
        if not (len(value) <= self.max_length):
            raise ValidationError(self.message, self.code)


class MinValueValidator(object):
    message = "Ensure minimum value is maintained"
    code = "min_value"

    def __init__(self, min_value, message=None):
        self.min_value = min_value
        if message is None:
            message = self.message
        self.message = message

    def __call__(self, value):
        if not (value >= self.min_value):
            raise ValidationError(self.message, self.code)


class MaxValueValidator(object):
    message = "Ensure maximum value is maintained"
    code = "max_value"

    def __init__(self, max_value, message=None):
        self.max_value = max_value
        if message is None:
            message = self.message
        self.message = message

    def __call__(self, value):
        if not (value <= self.max_value):
            raise ValidationError(self.message, self.code)


"""
if __name__ == "__main__":
    try:
        obj = MinLengthValidator( min_length=3, message="min length required")
        obj("ab")
    except ValidationError as exc:
        import ipdb; ipdb.set_trace()
        print(exc)
"""

