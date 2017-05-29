"""Determines whether a string has balanced, open, or closed parens."""
from stack import Stack


def eval_parens(input):
    """Evaluate whether a string has balanced, open, or closed parens."""
    print('input type:', type(input))
    if type(input) != str:
        raise TypeError('Please enter a string.')
    if '(' not in input and ')' not in input:
        raise ValueError('No parentheses in the string.')
    parens_stack = Stack()
    for char in input:
        if char == '(':
            parens_stack.push('open')
        if char == ')':
            try:
                parens_stack.pop()
            except IndexError:
                return -1
    return (1 if len(parens_stack) > 0 else 0)
