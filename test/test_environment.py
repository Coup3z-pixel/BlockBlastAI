import unittest

import pytest

from game.Environment import Environment


class MyTest(unittest.TestCase):
    def setup_method(self, test_method):
        self.env = Environment()

    def teardown_method(self, test_method):
        pass

    def test_reset(self):
        state = self.env.reset()

        assert len(state) == 4
        assert isinstance(state, list)
        assert isinstance(state[0], list)
        assert isinstance(state[0][0], list)
        assert isinstance(state[0][0][0], int)

    def test_method2(self):
        assert 0 == 0
