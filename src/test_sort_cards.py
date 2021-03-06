"""Test sort_cards.py. Parameters from Code Wars kata."""

import pytest

TEST_CARDS = [
    (['A'], ['A']),
    (['3'], ['3']),
    (['T'], ['T']),
    (['T', '8', '2', '4', 'Q'], ['2', '4', '8', 'T', 'Q']),
    (['Q', 'K', 'J', '6', '9', '3', '2'], ['2', '3', '6', '9', 'J', 'Q', 'K']),
    (['J', '6', '9', '3', '2', '7', 'A', '8'], ['A', '2', '3', '6', '7', '8', '9', 'J']),
    (['J', '6', '7', '9', 'J', '7', '3', '2', '7', 'A', '8'], ['A', '2', '3', '6', '7', '7', '7', '8', '9', 'J', 'J']),
    (['T', 'A', '8', 'A', 'A', 'A', '2', '4', 'A', 'Q', 'A'], ['A', 'A', 'A', 'A', 'A', 'A', '2', '4', '8', 'T', 'Q']),
    (['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']),
    (['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    (['Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    (['5', '4', 'T', 'Q', 'K', 'J', '6', '9', '3', '2', '7', 'A', '8'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']),
    (['Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T', 'Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T'], ['A', 'A', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', 'T', 'T', 'J', 'J', 'Q', 'Q', 'K', 'K']),
    (['Q', '2', '8', '6', 'J', 'K', 'K', 'K', 'K', 'K', '3', '9', '5', 'A', 'A', 'A', '4', '7', 'T', 'Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T'], ['A', 'A', 'A', 'A', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', 'T', 'T', 'J', 'J', 'Q', 'Q', 'K', 'K', 'K', 'K', 'K', 'K']),
    (['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T', 'Q', '2', '8', '6', 'J', 'K', '3', '9', '5', 'A', '4', '7', 'T'], ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', 'T', 'T', 'J', 'J', 'Q', 'Q', 'K', 'K'])
]


@pytest.mark.parametrize('input, result', TEST_CARDS)
def test_sort_cards(input, result):
    """Test the output of the card sorting function."""
    from sort_cards import sort_cards
    assert sort_cards(input) == result


def test_non_valid_card():
    """Test raises proper error."""
    from sort_cards import sort_cards
    with pytest.raises(KeyError):
        sort_cards(['A', 'B'])
