"""Tests for parenthetics.py."""
import pytest

PARENS_TABLE = [
    ('()()()', 0),
    ('()(', 1),
    (')', -1),
    (')(', -1),
    ('hello i am a cake)', -1),
    ('hello (i am a) cake', 0),
    ('((())', 1),
    ('))((', -1),
    ('''
        This is ( a )
        multiline
        string ()
        ''', 0)
]


@pytest.mark.parametrize('string, result', PARENS_TABLE)
def test_parens(string, result):
    """Test result."""
    from parenthetics import eval_parens
    assert eval_parens(string) == result


def test_arg_int():
    """Test dequeue on empty queue raises error."""
    from parenthetics import eval_parens
    with pytest.raises(TypeError):
        eval_parens(3)


def test_arg_list():
    """Test dequeue on empty queue raises error."""
    from parenthetics import eval_parens
    with pytest.raises(TypeError):
        eval_parens(['cake', '()', 'pie'])


def test_arg_tuple():
    """Test dequeue on empty queue raises error."""
    from parenthetics import eval_parens
    with pytest.raises(TypeError):
        eval_parens(('(', ')'))


def test_string_no_parens():
    """Test dequeue on empty queue raises error."""
    from parenthetics import eval_parens
    with pytest.raises(ValueError):
        eval_parens('cake')
