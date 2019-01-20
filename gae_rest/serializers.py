from gae_rest.exceptions import ValidationError
from gae_rest.validators import MinLengthValidator, MaxLengthValidator
from gae_rest.fields import StringField, IntegerField

class Serializer(object):

    """
    Return the validated_data
    Raise `serializers.ValidationError` on failure
    """
    def to_internal_value(self, data):
        pass
        """
        1. data should be a dict only. else raise error
        2. for each field in this serializer do
                find the validated_value. else add to validation errors list
                build a dict containing source field name and its value(s)

        return dict

        """

    """
    Return the primative output representation
    """
    def to_representation(self, instance):
        pass
        """
        1. for each field in this seriazlier do
                find native value
                build a dict containing source field name and its native value
        """

    # If you want to support `.save` then either or both of these

    """
    Save and return the created instance
    """
    def create(self, validated_data):
        pass

    """
    Save and return the updated instance
    """
    def update(self, instance, validated_data):
        pass


"""
Why its needed?
    + to have list of declared fields on which we can iterate to find what all fields are declared on a serializer
Why its needs to be a metaclass? Why need to override __new__ method of a serializer class?
"""
class SerializerMetaclass(object):
    pass

