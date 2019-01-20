import pytest
from gae_rest import serializers


class TestMinLengthValidator(object):

    def test_fails_if_lesser_than_min_length(self):
        min_length = serializers.MinLengthValidator(min_length=3)
        with pytest.raises(serializers.ValidationError) as excinfo:
            min_length('ab')
        assert excinfo.value.message == 'Ensure value maintains minimum length required'

    def test_equal_greater_than_min_length(self):
        min_length = serializers.MinLengthValidator(min_length=3)
        min_length('abc')


class TestMaxLengthValidator(object):

    def test_fails_if_greater_than_max_length(self):
        max_length = serializers.MaxLengthValidator(max_length=2)
        with pytest.raises(serializers.ValidationError) as excinfo:
            max_length('abc')
        assert excinfo.value.message == "Ensure value doesn't exceed maximum length required"

    def test_equal_lesser_than_max_length(self):
        max_length = serializers.MaxLengthValidator(max_length=3)
        max_length('abc')

