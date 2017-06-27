"""Determine whether a string is within the composite string of data from a linked list."""


class Node(object):
    """Methods of a Node object."""

    def __init__(self, data=None, next_node=None):
        """Instantiante a Node."""
        self.data = data
        self.next_node = next


class LinkedList(object):
    """Methods of a LinkedList object."""

    def __init__(self, head=None):
        """Instantiante a Linked List."""
        self.head = head

    def insert(self, data=None):
        """Insert a new Node."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


def find_string_ll(ll, string):
    """Determine whether a string is in the composite string of data from a linked list."""
    if len(string) == 0:
        raise ValueError('Can\'t check against an empty string.')
    current_node = ll.head
    stored_string = ''
    while current_node is not None:
        stored_string += current_node.data
        current_node = current_node.next_node
    if string in stored_string:
        return True
    return False
