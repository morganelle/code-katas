"""Module that determines whether a string has balanced, open, or closed parens."""
from stack import Stack


def eval_parens(input):
    """Evaluate whether a string has balanced, open, or closed parens."""
    print('input type:', type(input))
    if type(input) != str:
        raise TypeError('Please enter a string.')
    if len(input) < 1 or '(' not in input or ')' not in input:
        assert ValueError('Please enter a string with one or more characters, at least one of which is a an opening or closing parentheses.')
    parens_stack = Stack()
    for char in input:
        if char == '(':
            parens_stack.push('open')
        if char == ')':
            try:
                parens_stack.pop()
            except IndexError:
                return -1
    if len(parens_stack) > 0:
        return 1
    elif len(parens_stack) == 0:
        return 0
