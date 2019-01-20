# coding: utf-8


"""
test basic working of fields like StringField, IntegerField
these fields corresponds to html5 form input elements like <input type="text">, <select>
"""
import pytest
from gae_rest import serializers


class TestStringField(object):
    def test_if_stripped_by_default(self):
        field = serializers.StringField()
        assert field.to_internal_value(' abc ') == 'abc'

    def test_if_trim_whitespace_false(self):
        field = serializers.StringField(trim_whitespace=False)
        assert field.to_internal_value(' abc ') == ' abc '

    def test_not_allow_blank(self):
        field = serializers.StringField()
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation('')
        assert excinfo.value.message == 'blank is not allowed'

    def test_allow_blank(self):
        field = serializers.StringField(allow_blank=True, trim_whitespace=True)
        assert field.run_validation(' ') == ''

    def test_not_allow_null(self):
        field = serializers.StringField(allow_null=False, trim_whitespace=True)
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation(None)
        assert excinfo.value.message == 'null is not allowed'

    def test_allow_null(self):
        field = serializers.StringField(allow_null=True, trim_whitespace=True)
        value = field.run_validation(None)
        assert value is None

    def test_min_length(self):
        field = serializers.StringField(min_length=3)
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation('ab')
        assert isinstance(excinfo.value.message, list)
        e1 = excinfo.value.message[0]
        assert e1.message == 'Ensure this field has atleast 3 characters'

    def test_max_length(self):
        field = serializers.StringField(max_length=3)
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation('abcd')
        assert isinstance(excinfo.value.message, list)
        e1 = excinfo.value.message[0]
        assert e1.message == 'Ensure this field has maximum 3 characters'


class TestIntegerField(object):
    def test_non_integer(self):
        field = serializers.IntegerField()
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation(0.1)
        assert excinfo.value.message == 'Must be an integer value'

    def test_integer_value(self):
        field = serializers.IntegerField()
        field.run_validation(0)

    def test_required(self):
        field = serializers.IntegerField(required=False)
        assert field.to_internal_value(None) is None

    def test_default(self):
        field = serializers.IntegerField(default=-1, allow_null=True)
        assert field.to_internal_value(None) == -1

    def test_if_not_allow_null(self):
        field = serializers.IntegerField()
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation(None)
        assert excinfo.value.message == 'null is not allowed'

    def test_allow_null(self):
        field = serializers.IntegerField(allow_null=True)
        assert field.to_internal_value(None) is None

    def test_min_value(self):
        field = serializers.IntegerField(min_value=0)
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation(-1)
        obj = excinfo.value.message[0]
        assert obj.message == 'Ensure minimum value is 0'

    def test_max_value(self):
        field = serializers.IntegerField(max_value=10)
        with pytest.raises(serializers.ValidationError) as excinfo:
            field.run_validation(11)
        obj = excinfo.value.message[0]
        assert obj.message == 'Ensure maximum value is 10'

