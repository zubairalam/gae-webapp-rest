# coding: utf-8

from gae_rest.exceptions import _get_error_detail, ValidationError


class TestException(object):
    # def test_get_error_detail(self):
        # errors_list = [
                # ValidationError('e1', 'c1'),
                # ValidationError('e2', 'c2'),
                # ValidationError('e3', 'c3'),
                # ]
        # errors_dict = {
                # 'field1': 'error for field1',
                # 'field2': 'error for field2'
                # }
        # err = _get_error_detail(errors_list, 'default_code')
        # assert len(err) == 3
        # e1 = err[0]
        # assert e1.message == 'e1'
        # assert e1.code == 'c1'

        # err2 = _get_error_detail(errors_dict, 'default_code')
        # assert err2

