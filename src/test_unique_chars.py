"""Test for unique characters kata."""
import pytest


UNIQUE_CHAR_PARAMS = [
    (['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'], 'BbBb'),
    (['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'], 'foo'),
    (['a b c', 'bac', '3', 'baaaaccaaa a'], '3'),
    (['no', 'yes', 'YES', 'esssy'], 'no'),
    (['yes', 'YES', 'esssy', 'no'], 'no')
]


@pytest.mark.parametrize('strings, result', UNIQUE_CHAR_PARAMS)
def test_unique_chars(strings, result):
    """."""
    from unique_chars import find_uniq
    assert find_uniq(strings) == result


def test_non_valid_input_int():
    """Test raises proper error."""
    from unique_chars import find_uniq
    with pytest.raises(ValueError):
        find_uniq(15)


def test_non_valid_input_string():
    """Test raises proper error."""
    from unique_chars import find_uniq
    with pytest.raises(ValueError):
        find_uniq('cake')


def test_non_valid_input_in_list_end():
    """Test raises proper error."""
    from unique_chars import find_uniq
    with pytest.raises(ValueError):
        find_uniq(['qwwer', 'cake', 14])


def test_non_valid_input_in_list_middle():
    """Test raises proper error."""
    from unique_chars import find_uniq
    with pytest.raises(ValueError):
        find_uniq(['qwwer', 14, 'cake'])
