"""Tests for running average kata."""
import pytest


RUNNING_AVG_PARAMS = [
    ((10, 11.5, 12), 11.17),
    ((1, 2, 3), 2.00),
    ([1], 1.00),
    ([1, 2], 1.50),
    ([5.00, 5.00, 5.00, 5.00], 5.00),
    ([-1, -3, -5], -3.00),
    ([0, 0, 0, 1], 0.25)
]


@pytest.mark.parametrize('inputs, result', RUNNING_AVG_PARAMS)
def test_running_avg(inputs, result):
    """Return valid average."""
    from running_average import running_average
    test_avg = running_average()
    for num in inputs:
        avg = test_avg(num)
    assert avg == result


def test_running_avg_type_string():
    """Test invalid input."""
    from running_average import running_average
    with pytest.raises(TypeError):
        running_average('a')


def test_running_avg_type_tuple():
    """Test invalid input."""
    from running_average import running_average
    with pytest.raises(TypeError):
        running_average((1, 2))
