"""
These exercises focus on different approaches for writing property-based tests.

Try to find more than one test case for each exercise and test the functions under test extensively.
"""

import pytest
from hypothesis import given, strategies as st

# Exercise 1: Use Hypothesis to test the `reversed` built-in function for lists


# Your strategy goes here
@given(st.lists(st.integers(), min_size=3, unique=True))
def test_reversed(l: list[int]):
    rev = list(reversed(l))
    assert l[0] == rev[-1]
    assert l[1] == rev[-2]


@given(st.lists(st.integers(), min_size=3, unique=True))
def test_reversed(l: list[int]):
    assert l == list(reversed(list(reversed(l))))


# Additional test cases go here


# Exercise 2: Use Hypothesis to test the `sorted` built-in function for lists.


# Your strategy goes here
def test_sorted():
    # Your test goes here
    pytest.skip()


# Additional test cases go here


# Exercise 3: Use Hypothesis to test the `enumerate` built-in function for lists.


# Your strategy goes here
def test_enumerated():
    # Your test goes here
    pytest.skip()
