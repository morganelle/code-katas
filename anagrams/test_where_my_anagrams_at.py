"""

Below are the tests from CodeWars.

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

"""
import pytest

ANAGRAM_TESTS = [
    ('abba', ['aabb', 'abcd', 'bbaa', 'dada'], ['aabb', 'bbaa']),
    ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'], ['carer', 'racer']),
    ('laser', ['lazing', 'lazy', 'lacer'], []),
    ('hello123', ['32h1ello', 'hello', 'he ello'], ['32h1ello']),
    ('hello', ['32h1ello', 'he ello'], []),
    ('Hello', ['hello', 'he ello'], []),
    ('#$', ['$#', '#h$'], ['$#'])
]


@pytest.mark.parametrize('word, words, result', ANAGRAM_TESTS)
def test_anagrams(word, words, result):
    """Test the output from the anagrams function."""
    from where_my_anagrams_at import anagrams
    assert anagrams(word, words) == result
