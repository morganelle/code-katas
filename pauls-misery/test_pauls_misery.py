"""
Below are the tests from CodeWars.

Test.assert_equals(paul(['life', 'eating', 'life']), 'Super happy!')
Test.assert_equals(paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']), 'Super happy!')
Test.assert_equals(paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']), 'Happy!')

"""
import pytest

MISERY_TEST = [
    (['life', 'eating', 'life'], 'Super happy!'),
    (['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating'], 'Super happy!'),
    (['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating'], 'Happy!'),
    ([''], 'Super happy!'),
    (['Pete\'s kata'], 'Super happy!'),
    (['Pete\'s kata','Pete\'s kata','Pete\'s kata','Pete\'s kata','Pete\'s kata'], 'Super happy!'),
    (['Kata', 'Kata', 'Kata'], 'Super happy!')
]


@pytest.mark.parametrize('list, result', MISERY_TEST)
def test_pauls_misery(list, result):
    """Test the output from the anagrams function."""
    from pauls_misery import paul
    assert paul(list) == result
