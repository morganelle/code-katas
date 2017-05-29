"""

Below are the tests from CodeWars.

testing(no_boring_zeros(1450), 145)
testing(no_boring_zeros(960000), 96)
testing(no_boring_zeros(1050), 105)
testing(no_boring_zeros(-1050), -105)
testing(no_boring_zeros(0), 0)


"""
import pytest

ZEROS_TESTS = [
    (1450, 145),
    (960000, 96),
    (1050, 105),
    (-1050, -105),
    (0, 0),
    (1000 - 100, 9),
    (-60 - 60, -12),
    (0 + 0, 0),
    (10101010, 1010101)
]


@pytest.mark.parametrize('num, result', ZEROS_TESTS)
def test_no_boring_zeros(num, result):
    """Test the output from the anagrams function."""
    from no_zeros_for_heros import no_boring_zeros
    assert no_boring_zeros(num) == result
