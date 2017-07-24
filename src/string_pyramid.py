"""Build a pyramid of characters from a given string."""


def watch_pyramid_from_the_side(characters):
    """Return a string pyramid from the side view."""
    try:
        pyramid_side = ''
        pyr_width = 2 * len(characters) - 1
        for i, letter in enumerate(characters[::-1]):
            pyramid_side += '{:{align}{width}}\n'.format(
                (letter * (2 * i + 1)),
                align='^',
                width=pyr_width
            )
        return pyramid_side[:-1]
    except:
        return


def watch_pyramid_from_above(characters):
    """Return a string pyramid from the top view."""
    try:
        pyramid_above = watch_pyramid_from_the_side(characters).split('\n')[::-1]
        pyramid_str = ''
        for i in range(len(pyramid_above)):
            pyramid_above_str = ''
            for j, letter in enumerate(pyramid_above[i]):
                if letter == ' ':
                    letter = pyramid_above[i - 1][j]
                pyramid_above_str += letter
            pyramid_above[i] = pyramid_above_str
        for i in range(len(pyramid_above) - 2, -1, -1):
            pyramid_above.append(pyramid_above[i])
        for row in pyramid_above:
            pyramid_str += row + '\n'
        return pyramid_str[:-1]
    except:
        return


def count_visible_characters_of_the_pyramid(characters):
    """Return the top-level dimensions of a string pyramid."""
    return (2 * len(characters) - 1) ** 2 if characters else -1


def count_all_characters_of_the_pyramid(characters):
    """."""
    return sum([((2 * n + 1) ** 2) for n in range(len(characters))]) if characters else -1
