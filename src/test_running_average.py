"""Tests for running average kata."""
import pytest


RUNNING_AVG_PARAMS = [
    ((10, 11.5, 12), 11.17),
    ((1, 2, 3), 2.00),
    ([1], 1.00),
    ([1, 2], 1.50)
]


@pytest.mark.parametrize('inputs, result', RUNNING_AVG_PARAMS)
def test_running_avg(inputs, result):
    """Return valid average."""
    from running_average import running_average
    test_avg = running_average()
    for num in inputs:
        avg = test_avg(num)
    assert avg == result
