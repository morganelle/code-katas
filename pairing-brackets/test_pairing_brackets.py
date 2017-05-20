"""
Below are the tests from CodeWars.

Test.assert_equals(bracket_pairs("len(list)"),{3:8},"Single pair of brackets")
Test.assert_equals(bracket_pairs("def f(x"),False,"unmatched bracket")
Test.assert_equals(bracket_pairs("(a(b)c()d)"),{0:9,2:4,6:7},"nested brackets")

"""
import pytest


BRACKET_TEST = [
    ("len(list)", {3: 8}),
    ("def f(x", False),
    ("(a(b)c()d)", {0: 9, 2: 4, 6: 7}),
    ('((()))', {0: 5, 1: 4, 2: 3}),
    ('()()()', {0: 1, 2: 3, 4: 5}),
    ('(()())', {0: 5, 1: 2, 3: 4}),
    ('))', False)
]


@pytest.mark.parametrize('string, result', BRACKET_TEST)
def test_bracket_pairs(string, result):
    """Test the output from the anagrams function."""
    from pairing_brackets import bracket_pairs
    assert bracket_pairs(string) == result
