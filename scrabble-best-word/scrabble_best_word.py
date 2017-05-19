"""

Kata: Scrabble best word

#1 Best Practices Solution by CrazyMerlyn

def get_best_word(points, words):
    points = dict(zip(uppercase, points))

    score = lambda word: sum(points[c] for c in word)

    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])


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


def get_best_word(point_list, words):
    """Return highest-point, shortest, or first shortest word for given lists of words and associated points."""
    scores = []
    winners = []
    for word in words:
        count = 0
        for letter in word:
            count = count + point_list[ord(letter) - 65]
        scores.append(count)
    word_dict = list(zip(words, scores))
    scores.sort(reverse=True)
    word_dict.sort(key=lambda x: x[1], reverse=True)
    best_score = scores[0]
    if scores.count(best_score) > 1:
        for item in word_dict:
            if item[1] == best_score:
                winners.append(item[0])
        winners.sort(key=lambda x: len(x))
        return words.index(winners[0])
    else:
        return words.index(word_dict[0][0])
