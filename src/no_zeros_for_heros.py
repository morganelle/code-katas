"""

Kata: No zeros for heros

#1 Best Practices Solution by zebulan, Bestesterer

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


Instructions
----------------------------------------------------------------------
Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105

Zero alone is fine, don't worry about it. Poor guy anyway

"""


def no_boring_zeros(n):
    """Remove 0s from end of number and return it."""
    while n % 10 == 0 and n != 0:
        n = n // 10
    return n
