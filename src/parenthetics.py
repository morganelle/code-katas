"""Determines whether a string has balanced, open, or closed parens."""
from stack import Stack


def eval_parens(user_string):
    """Evaluate whether a string has balanced, open, or closed parens."""
    print('input type:', type(user_string))
    if type(user_string) != str:
        raise TypeError('Please enter a string.')
    if '(' not in user_string and ')' not in user_string:
        raise ValueError('No parentheses in the string.')
    parens_stack = Stack()
    for char in user_string:
        if char == '(':
            parens_stack.push('open')
        if char == ')':
            try:
                parens_stack.pop()
            except IndexError:
                return -1
    return 1 if len(parens_stack) > 0 else 0
