import pytest

from pi import *


def test_incorrect_int_input():
    assertTrue = checkLength(16)


def test_input_is_string():
    assertTrue = checkString('pi')


def test_pi():
    assert "PI to 5 decimal places is: 3.14159" == getPi(5)
