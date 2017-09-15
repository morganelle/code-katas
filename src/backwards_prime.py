"""Backwards Read Primes

Description:

Backwards Read Primes are primes that when read backwards in base 10
(from right to left) are a different prime. (This rules out primes
which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31
which is prime too. Same for the others.

Task

Find all Backwards Read Primes between two positive given numbers
(both inclusive), the second one being greater than the first one.
The resulting array or the resulting string will be ordered following
the natural order of the prime numbers.

Example

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] backwardsPrime
(9900, 10000) => [9923, 9931, 9941, 9967]

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
"""

from math import sqrt


def prime(n):
    """Return True if a number is a prime, False if not."""
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def backwards_prime(lower, upper):
    """Return a list of integers that are prime ."""
    if lower % 2 == 0:
        lower = lower + 1
    return [i for i in range(lower, upper + 1, 2) if prime(i) and str(i)[::-1] != str(i) and prime(int(str(i)[::-1]))]
