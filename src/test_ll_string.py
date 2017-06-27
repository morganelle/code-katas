"""Tests for ll_string module."""
from ll_string import LinkedList, find_string_ll
import pytest


@pytest.fixture
def linked_list_1():
    """."""
    test_ll = LinkedList()
    test_ll.insert('ck')
    test_ll.insert('Ni')
    test_ll.insert('is')
    test_ll.insert('e')
    test_ll.insert('ynam')
    test_ll.insert('m')
    return test_ll


@pytest.fixture
def linked_list_2():
    """."""
    test_ll2 = LinkedList()
    test_ll2.insert('text')
    test_ll2.insert('is')
    test_ll2.insert('this')
    return test_ll2


def test_empty_string_raises_error(linked_list_1):
    """."""
    with pytest.raises(ValueError):
        find_string_ll(linked_list_1, '')


def test_ll_1_true(linked_list_1):
    """."""
    assert find_string_ll(linked_list_1, 'Nick') is True


def test_ll_1_false(linked_list_1):
    """."""
    assert find_string_ll(linked_list_1, 'nick') is False


def test_ll_2_true(linked_list_2):
    """."""
    assert find_string_ll(linked_list_2, 'isist') is True


def test_ll_2_false(linked_list_2):
    """."""
    assert find_string_ll(linked_list_2, 'tt') is False
