"""Kata that takes scrambled string of number words and returns an ordered string of numeric characters.

Kata: Original Number

Best Practices Solution by Blind4Basics:

    from collections import Counter

    EXECUTIONS_ORDER = [('Z', Counter("ZERO"),  '0'),
                        ('W', Counter("TWO"),   '2'),
                        ('U', Counter("FOUR"),  '4'),
                        ('X', Counter("SIX"),   '6'),
                        ('G', Counter("EIGHT"), '8'),
                        ('O', Counter("ONE"),   '1'),
                        ('H', Counter("THREE"), '3'),
                        ('F', Counter("FIVE"),  '5'),
                        ('V', Counter("SEVEN"), '7'),
                        ('I', Counter("NINE"),  '9')]

    def original_number(s):
        ans, count, executions = [], Counter(s), iter(EXECUTIONS_ORDER)
        while count:
            c, wordCount, value = next(executions)
            ans.extend([value]*count[c])
            for _ in range(count[c]): count -= wordCount
        return ''.join(sorted(ans))

Instructions
----------------------------------------------------------------------
John has an important number, and he doesn't want others to see it.

He decided to encrypt the number, using the following steps:

His number is always a non strict increasing sequence
ie. "123"

He converted each digit into English words.
ie. "123"--> "ONETWOTHREE"

And then, rearrange the letters randomly.
ie. "ONETWOTHREE" --> "TTONWOHREEE"
John felt that his number were safe in doing so. In fact, such encryption can
be easily decrypted :(

Given the encrypted string s, your task is to decrypt it, return the original
number in string format.

Note, You can assume that the input string s is always valid; It contains only
uppercase Letters; The decrypted numbers are arranged in ascending order;
The leading zeros are allowed.

Example

For s = "ONE", the output should be 1.
For s = "EON", the output should be 1 too.
For s = "ONETWO", the output should be 12.
For s = "OONETW", the output should be 12 too.
For s = "ONETWOTHREE", the output should be 123.
For s = "TTONWOHREEE", the output should be 123 too.

"""


def original_number(scrambled_string):
    """Decrypt scrambled string and return an ordered string of numeric characters."""
    scrambled_list = list(scrambled_string.upper())
    num_chars = ['Z', 'W', 'U', 'X', 'G', 'O', 'T', 'F', 'S', 'I']
    decoded = []
    num_dict = {
        'Z': ['ZERO', '0', 0],
        'W': ['TWO', '2', 0],
        'U': ['FOUR', '4', 0],
        'X': ['SIX', '6', 0],
        'G': ['EIGHT', '8', 0],
        'O': ['ONE', '1', 0],
        'T': ['THREE', '3', 0],
        'F': ['FIVE', '5', 0],
        'S': ['SEVEN', '7', 0],
        'I': ['NINE', '9', 0]}
    for char in num_chars:
        for letter in scrambled_list:
            if letter == char:
                decoded.append(num_dict[char][1])
                num_dict[char][2] += 1
        if num_dict[char][2]:
            for i in range(num_dict[char][2]):
                for letter in num_dict[char][0]:
                    scrambled_list.remove(letter)
    return ''.join(sorted(decoded))
