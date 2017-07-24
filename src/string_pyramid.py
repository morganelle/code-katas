r"""

Kata: String Pyramid

#1 Best Practices Solution by Blind4Basics:

  def watch_pyramid_from_the_side(characters):
      if not characters : return characters
      baseLen = len(characters)*2-1
      return '\n'.join( ' '*(i) + characters[i]*(baseLen-2*i) + ' '*(i) for i in range(len(characters)-1,-1,-1) )


  def watch_pyramid_from_above(characters):
      if not characters : return characters
      baseLen = len(characters)*2-1
      return '\n'.join( characters[0:min(i,baseLen-1-i)] + characters[min(i,baseLen-1-i)]*(baseLen-2*min(i,baseLen-1-i)) + characters[0:min(i,baseLen-1-i)][::-1] for i in range(baseLen) )


  def count_visible_characters_of_the_pyramid(characters):
      return -1 if not characters else (len(characters)*2-1)**2


  def count_all_characters_of_the_pyramid(characters):
      return -1 if not characters else sum( (2*i+1)**2 for i in range(len(characters)) )


Instructions
----------------------------------------------------------------------
You have to build a pyramid.

This pyramid should be built from characters from a given string.

You have to create the code for these four methods:

  watch_pyramid_from_the_side(characters):
  watch_pyramid_from_above(characters):
  count_visible_characters_of_the_pyramid(characters):
  count_all_characters_of_the_pyramid(characters):

The first method ("FromTheSide") shows the pyramid as you would see from the
side.
The second method ("FromAbove") shows the pyramid as you would see from above.
The third method ("CountVisibleCharacters") should return the count of all
characters, that are visible from outside the pyramid.
The forth method ("CountAllCharacters") should count all characters of the
pyramid. Consider that the pyramid is completely solid and has no holes
or rooms in it.

Every character will be used for building one layer of the pyramid. So the
length of the given string will be the height of the pyramid. Every layer
will be built with stones from the given character. There is no limit
of stones. The pyramid should have perfect angles of 45 degrees.

Example: Given string: "abc"

Pyramid from the side:

  c
 bbb
aaaaa

Pyramid from above:

aaaaa
abbba
abcba
abbba
aaaaa

Count of visible stones/characters: 25

Count of all used stones/characters: 35

There is no meaning in the order or the choice of the characters.
It should work the same for example "aaaaa" or "54321".
If the string is null or empty, you should exactly return this value
for the watch-methods and -1 for the count-methods.

"""


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
