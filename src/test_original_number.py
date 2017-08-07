"""Test for original number kata."""
import pytest
from random import randint, random

ORIGINAL_NUMBER_PARAMS = [
    ('OTNWEO', '12'),
    ('ONETWOTHREE', '123'),
    ('OONETW', '12'),
    ('TTONWOHREEE', '123'),
    ('SSVNEETVEZNXIERNEENNIEETVEERIORONTTSZEFTIEVNEEENENHOOOVINSVXSREEOENIHTWSENEEESFIWEHRVW', '001222333556677777999')
]


def test_random_inputs():
    """Test randomly generated strings."""
    from original_number import original_number
    base = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

    for _ in range(40):
        sol = ''.join(sorted(str(randint(0, 9)) for q in range(randint(1, 25))))
        n = ''.join(sorted(''.join(base[int(l)] for l in sol), key=lambda a: random()))
        assert original_number(n) == sol


@pytest.mark.parametrize('input, result', ORIGINAL_NUMBER_PARAMS)
def test_original_number(input, result):
    """Test cases from kata."""
    from original_number import original_number
    assert original_number(input) == result
