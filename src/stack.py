"""Python implementation for stack data structure."""


class Stack(object):
    """Methods and attributes of Stack class."""

    def __init__(self):
        """Initialize empty Stack."""
        self.head = None
        self._length = 0

    def push(self, val=None):
        """Push new node to top of Stack."""
        if val is None:
            raise ValueError('Please add a value.')
        new_node = Node(val, self.head)
        self.head = new_node
        self._length += 1

    def pop(self):
        """Remove head of Stack."""
        current_node = self.head
        if current_node is None:
            raise IndexError('Nothing to pop.')
        self._length -= 1
        self.head = current_node.next_node
        return current_node

    def display(self):
        """Return string representing Stack as Python tuple."""
        display_string = u''
        current_node = self.head
        while current_node:
                display_string = '{} {}'.format(current_node.val,
                                                display_string)
                current_node = current_node.next_node
        display_string = display_string.strip().replace(' ', ', ')
        display_string = '({})'.format(display_string)
        return display_string

    def __len__(self):
        """Overwrite default len method."""
        return self._length


class Node(object):  # pragma: no cover
    """Set properties and methods for Stack class."""

    def __init__(self, val, next_node=None):
        """."""
        self.val = val
        self.next_node = next_node
