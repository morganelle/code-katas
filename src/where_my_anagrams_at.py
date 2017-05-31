"""

Kata: Where My Anagrams At?

#1 Best Practices Solution by sandbochs, Dru7-BY, fandogh, aposiker

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]


Instructions
----------------------------------------------------------------------
Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should
return an array of all the anagrams or an empty array if there are none.

"""


def anagrams(word, words):
    """Return a list of anagrams from a list of words for a given word."""
    results, word_sorted = [], ''.join(sorted(word))
    for w in words:
        if ''.join(sorted(w)) == word_sorted:
            results.append(w)
    return results
