import pytest
from math_it_up import is_even, is_odd, mean, median, mode

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

@pytest.mark.parametrize("inputs,expecteds", [(2, True), (3, False), (4, True)])
def test_is_even(inputs, expecteds):
    assert is_even(inputs) == expecteds

"""
Tests for the `is_even` function
"""

@pytest.mark.parametrize("input,expected", [(2, False), (3, True), (4, False)])
def test_is_odd(input, expected):
  assert is_odd(input) != expected

  """
  Tests for the `is_odd` function
  """

@pytest.fixture
def listy():
  return [1, 2, 4, 8, 16, 32]

def test_mean(listy):
  assert mean(listy) == 10.5

  """
  Tests for the `mean` function
  """

@pytest.fixture
def lists():
  return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test_median(lists):
  assert median(lists) == 5.5

  """
  Tests for the `median` function
  """

@pytest.fixture
def list():
  return [1, 4, 2, 4, 3, 4, 5]
def test_mode(list):
  assert mode(list) == [4]

  """
  Tests for the `mode` function
  """