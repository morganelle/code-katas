"""Kata that takes scrambled string of number words and returns an ordered string of numeric characters."""


def original_number(scrambled_string):
    """Decrypt scrambled string and return an ordered string of numeric characters.."""
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
