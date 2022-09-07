import datetime
import unittest
from trashcli.trash import Clock
from mock import Mock, call


class TestClock(unittest.TestCase):
    def setUp(self):
        self.errors = Mock(spec=['print_error'])

    def test_return_real_time(self):
        clock = Clock(lambda: 'now', {},
                      self.errors)

        result = clock.get_now_value()

        assert (result, []) == ('now', self.errors.mock_calls)

    def test_return_fake_time(self):
        clock = Clock(lambda: 'now',
                      {'TRASH_DATE': '2021-06-04T18:40:19'},
                      self.errors)

        result = clock.get_now_value()

        assert (result, []) == (datetime.datetime(2021, 6, 4, 18, 40, 19),
                                self.errors.mock_calls)

    def test_return_true_now_whe_fake_time_is_invalid(self):
        clock = Clock(lambda: 'now',
                      {'TRASH_DATE': 'invalid'},
                      self.errors)

        result = clock.get_now_value()

        assert (result,
                [call.print_error('invalid TRASH_DATE: invalid')]) == \
               ('now', self.errors.mock_calls)
