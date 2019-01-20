from gae_rest.exceptions import ValidationError
from gae_rest.validators import (MinLengthValidator, MaxLengthValidator,
        MinValueValidator, MaxValueValidator)


"""
A generic descriptor like class
Where it will be needed
Field
    + Why its needed.
        We need to create custom Fields like IntegerField, StringField
        this brings need to have some common attribute and behaviour in Field class
    + What all fields we are going to work with initially
        IntegerField
        StringField
"""


class Field(object):
    """
    Represents a field in a user facing html form
    """

    def __init__(self, **kwargs):
        self.required= kwargs.pop('required', True)
        self.allow_null = kwargs.pop('allow_null', False)
        self.default = kwargs.pop('default', None)
        self.validators = kwargs.pop('validators', [])

    def to_internal_value(self):
        """
        To internal representation
        e.g. an entity object (non serializable) or a primitive value
        """
        pass

    def to_representation(self):
        """
        To a serializable format
        """
        pass

    def bind(self, field_name, parent):
        """
        bind a field instance declared on a serializable to the serializable object with its field name and field instance
        This way we can maintain a mapping between (parent, field_name, field instance)
        """
        self.field_name = parent

    @property
    def validators(self):
        """
        Get list of validators defined to this field instance
        """
        return self._validators

    @validators.setter
    def validators(self, validators):
        """
        Set a list of validators to this field
        """
        self._validators = validators

    def run_validation(self, data):
        """
        Validate `data` value with all the validators defined on this field
        return internal value if all checks passes
        """
        value = self.to_internal_value(data)
        errors = []
        for validator in self.validators:
            try:
                validator(value)
            except ValidationError as exc:
                errors.append(exc.detail)
        if errors:
            raise ValidationError(errors)
        return value


class StringField(Field):
    """
    data is being stored on Serializer object, not on Field instance
    Field instance is not a descriptor, its a simple class
    """

    default_error_messages = {
            'min_length': 'Ensure this field has atleast {min_length} characters',
            'max_length': 'Ensure this field has maximum {max_length} characters',
            }

    def __init__(self, **kwargs):
        self.trim_whitespace = kwargs.pop('trim_whitespace', True)
        self.allow_blank = kwargs.pop('allow_blank', False)
        self.min_length = kwargs.pop('min_length', None)
        self.max_length = kwargs.pop('max_length', None)
        super(StringField, self).__init__(**kwargs)
        if self.min_length is not None:
            message = self.default_error_messages['min_length'].format(min_length=self.min_length)
            self.validators.append(MinLengthValidator(self.min_length, message=message))
        if self.max_length is not None:
            message = self.default_error_messages['max_length'].format(max_length=self.max_length)
            self.validators.append(MaxLengthValidator(self.max_length, message=message))

    def to_internal_value(self, data):
        """
        return internal representation that can be non serializable
        """
        return str(data.strip()) if self.trim_whitespace else str(data)

    def to_representation(self, data):
        """
        return serializable representation
        """
        return str(data)

    def run_validation(self, data):

        # data = None, allow_null=False
        if not self.allow_null:
            if data is None:
                raise ValidationError('null is not allowed', 'null')
        # data = None, allow_null=True
        if self.allow_null and data is None: return None

        if not self.allow_blank:
            if len(data) == 0 or (self.trim_whitespace and len(data.strip()) == 0):
                raise ValidationError('blank is not allowed', 'blank')

        return super(StringField, self).run_validation(data)


class IntegerField(Field):
    error_messages = {
            'min_value': 'Ensure minimum value is {min_value}',
            'max_value': 'Ensure maximum value is {max_value}',
            }
    def __init__(self, **kwargs):
        self.min_value = kwargs.pop('min_value', None)
        self.max_value = kwargs.pop('max_value', None)
        super(IntegerField, self).__init__(**kwargs)
        if self.min_value is not None:
            self.validators.append(MinValueValidator(min_value=self.min_value, message=self.error_messages['min_value'].format(min_value=self.min_value)))
        if self.max_value is not None:
            self.validators.append(MaxValueValidator(max_value=self.max_value, message=self.error_messages['max_value'].format(max_value=self.max_value)))

    def is_integer(self, data):
        # not a unicode
        if isinstance(data, str):
            return False
        # allow decimal 1.0 only
        decimal_data = str(data).split('.')
        if len(decimal_data) == 2:
            if int(decimal_data[1]) != 0:
                return False
        return True

    def to_internal_value(self, data):
        if self.allow_null or not self.required:
            if data is None:
                if self.default: return self.default
                else: return data
        if data is None and (not self.allow_null or self.required):
            raise ValidationError('null is not allowed', 'null')
        if not self.is_integer(data):
            raise ValidationError('Must be an integer value', 'invalid')
        return data

