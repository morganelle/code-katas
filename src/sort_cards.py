"""Priority queue implementation of card-sorting kata.

#1 Best Practices Solution by zebulan and others:

    def sort_cards(cards):
        return sorted(cards, key="A23456789TJQK".index)

Instructions
----------------------------------------------------------------------
Write a function sort_cards() that sorts a shuffled list of cards,
so that any given list of cards is sorted by rank, no matter the
starting collection.

All cards in the list are represented as strings, so that sorted
list of cards looks like this:

['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Example:

sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
returns ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

Hint: Tests will have many occurrences of same rank cards, as well as vary in
length. You can assume though, that input list is always going to have at
least 1 element.

"""

from priority_que import PriorityQ


def sort_cards(cards):
    """Return a list of sorted cards."""
    priority_q = PriorityQ()
    face_cards = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    for card in cards:
        try:
            deck_priority = int(card)
        except ValueError:
            deck_priority = face_cards[card]
        priority_q.insert(card, priority=deck_priority)
    return [card for priority, card in priority_q._list]
