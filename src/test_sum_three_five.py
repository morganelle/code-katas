"""Tests for sum of all sum_three_five module."""

import pytest

BACKWARDS_PRIME_TEST = [
    (10, 23),
    (20, 78),
    (0, 0),
    (1, 0),
    (200, 9168)
]


@pytest.mark.parametrize('upper, result', BACKWARDS_PRIME_TEST)
def test_sum_three_five(upper, result):
    """Test backwards prime function."""
    from sum_three_five import solution
    assert solution(upper) == result
