# -*- coding: utf-8 -*-

import pytest
from temp_project.skeleton import fib

__author__ = "Lachlan McLachlan"
__copyright__ = "Lachlan McLachlan"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
