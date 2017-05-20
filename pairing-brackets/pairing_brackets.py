"""
Kata: Pairing brackets

#1 Best Practices Solution by biskinis

def bracket_pairs(string):
    brackets = {}
    open_brackets = []

    for i, c in enumerate(string):
        if c == '(':
            open_brackets.append(i)
        elif c == ')':
            if not open_brackets:
                return False
            brackets[open_brackets.pop()] = i

    return False if open_brackets else brackets


Instructions
----------------------------------------------------------------------
You're playing to scrabble. But counting points is hard.

You decide to create a little script to calculate the best possible value.

The function takes two arguments :

points : an array of integer representing for each letters from A to Z the
points that it pays words : an array of strings, uppercase

You must return the index of the shortest word which realize the highest
score. When there are two or more words having same score, then the index
of the smallest word should be returned

If also the length is the same, then return the index of the first one.


"""


def bracket_pairs(string):
    """Return a dictionary with open/close position pairs."""
    bracket_list = []
    if string.count('(') != string.count(')') or string.find('(') > string.find(')'):
        return False
    for i in range(len(string)):
        if string[i] == '(':
            bracket_list.append([i, None])
        elif string[i] == ')':
            for j in range(len(bracket_list) - 1, -1, -1):
                if bracket_list[j][1] is None:
                    bracket_list[j][1] = i
                    break
    return dict(bracket_list)
