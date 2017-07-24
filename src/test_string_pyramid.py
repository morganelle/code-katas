"""

Below are the tests from CodeWars.

# None or Empty
Test.describe('None or Empty Tests')
Test.it('should handle None and empty')
Test.assert_equals(watch_pyramid_from_the_side(None), None)
Test.assert_equals(watch_pyramid_from_above(None), None)
Test.assert_equals(count_visible_characters_of_the_pyramid(None), -1)
Test.assert_equals(count_all_characters_of_the_pyramid(None), -1)
Test.assert_equals(watch_pyramid_from_the_side(''), '')
Test.assert_equals(watch_pyramid_from_above(''), '')
Test.assert_equals(count_visible_characters_of_the_pyramid(''), -1)
Test.assert_equals(count_all_characters_of_the_pyramid(''), -1)

# Basic Tests
Test.describe('Basic Tests')
Test.it('should handle 2 characters')
characters = '*#'
expected_watch_from_side = '''\
 #
***'''
expected_watch_from_above = '''\
***
*#*
***'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(
    expected_watch_from_side, expected_watch_from_above,
    actual_watch_from_side, actual_watch_from_above
)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 9)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 10)

Test.it('should handle 3 characters')
characters = 'abc'
expected_watch_from_side = '''\
  c
 bbb
aaaaa'''
expected_watch_from_above = '''\
aaaaa
abbba
abcba
abbba
aaaaa'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(
    expected_watch_from_side, expected_watch_from_above,
    actual_watch_from_side, actual_watch_from_above
)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 25)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 35)

Test.it('should handle 3 same characters')
characters = 'aaa'
expected_watch_from_side = '''\
  a
 aaa
aaaaa'''
expected_watch_from_above = '''\
aaaaa
aaaaa
aaaaa
aaaaa
aaaaa'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(expected_watch_from_side, expected_watch_from_above,
              actual_watch_from_side, actual_watch_from_above)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 25)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 35)

Test.it('should handle 5 descending ordered characters')
characters = '54321'
expected_watch_from_side = '''\
    1
   222
  33333
 4444444
555555555'''

expected_watch_from_above = '''\
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555'''
actual_watch_from_side = watch_pyramid_from_the_side(characters)
actual_watch_from_above = watch_pyramid_from_above(characters)
visualisation(expected_watch_from_side, expected_watch_from_above,
              actual_watch_from_side, actual_watch_from_above)
Test.assert_equals(count_visible_characters_of_the_pyramid(characters), 81)
Test.assert_equals(count_all_characters_of_the_pyramid(characters), 165)

"""

import pytest


PARAMS_PYRAMID_SIDE = [
    ('abc', '  c  \n bbb \naaaaa'),
    ('aaa', '  a  \n aaa \naaaaa'),
    ('54321', '    1    \n   222   \n  33333  \n 4444444 \n555555555'),
    ('*#', ' # \n***'),
    ('1', '1'),
    ('', ''),
    (None, None)
]

PARAMS_PYRAMID_ABOVE = [
    ('abc', '''\
aaaaa
abbba
abcba
abbba
aaaaa'''),
    ('aaa', '''\
aaaaa
aaaaa
aaaaa
aaaaa
aaaaa'''),
    ('54321', '''\
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555'''),
    ('*#', '***\n*#*\n***'),
    ('1', '1'),
    ('', ''),
    (None, None)
]

PARAMS_STONES_VISIBLE = [
    ('abc', 25),
    ('54321', 81),
    ('*#', 9),
    ('1', 1),
    ('', -1),
    (None, -1)
]

PARAMS_STONES_ALL = [
    ('abc', 35),
    ('54321', 165),
    ('*#', 10),
    ('1', 1),
    ('', -1),
    (None, -1)
]


@pytest.mark.parametrize('input, result', PARAMS_PYRAMID_SIDE)
def test_side_view(input, result):
    """Test the output from the anagrams function."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(input) == result


@pytest.mark.parametrize('input, result', PARAMS_PYRAMID_ABOVE)
def test_above_view(input, result):
    """Test the output from the anagrams function."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(input) == result


@pytest.mark.parametrize('input, result', PARAMS_STONES_VISIBLE)
def test_count_visible(input, result):
    """Test the output from the anagrams function."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(input) == result


@pytest.mark.parametrize('input, result', PARAMS_STONES_ALL)
def test_count_all(input, result):
    """Test the output from the anagrams function."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(input) == result
