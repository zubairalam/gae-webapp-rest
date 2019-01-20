from gae_webapp_rest import ModelSerializer

from models import App


class AppSerializer(ModelSerializer):

    class Meta:
        model = App

```
usages:

serializer = AppSerializer(data=request.DATA)

# Perform all validation on serializer object only 
serializer.is_valid()

# validated_data in premitive format
serializer.validated_data

# Instantiate and save a model instance to the database. 
serializer.save()

```


class BaseSerializer(object):

    """
    Return the validated_data
    Raise `serializers.ValidationError` on failure
    """
    def to_internal_value(self, data):
        pass

    """
    Return the primative output representation
    """
    def to_representation(self, instance):
        pass

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
