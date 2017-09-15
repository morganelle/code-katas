"""Tests for backwards prime module."""

import pytest

BACKWARDS_PRIME_TEST = [
    (7000, 7100, [7027, 7043, 7057]),
    (70000, 70245, [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]),
    (70485, 70600, [70489, 70529, 70573, 70589]),
    (60000, 70000, []),
    (109500, 109700, [109537, 109579, 109583, 109609, 109663]),
    (1095000, 1095403, [1095047, 1095209, 1095319, 1095403]),
    (100, 403, [107, 113, 149, 157, 167, 179, 199, 311, 337, 347, 359, 389]),
    (400, 503, []),
    (7048500, 7048600, [7048519, 7048579]),
    (1048500, 1048600, [1048571, 1048583]),
    (1000001, 1000100, [1000033, 1000037, 1000039]),
    (700000008, 700000050, [700000031])
]


@pytest.mark.parametrize('lower, upper, result', BACKWARDS_PRIME_TEST)
def test_backwards_prime(lower, upper, result):
    """Test backwards prime function."""
    from backwards_prime import backwards_prime
    assert backwards_prime(lower, upper) == result
