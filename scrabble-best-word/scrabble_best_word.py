"""

Kata: Scrabble best word

#1 Best Practices Solution by CrazyMerlyn

def get_best_word(points, words):
    points = dict(zip(uppercase, points))

    score = lambda word: sum(points[c] for c in word)

    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])


Instructions
----------------------------------------------------------------------
Write a function which outputs the positions of matching bracket pairs.
The output should be a dictionary with keys the positions of the open brackets
'(' and values the corresponding positions of the closing brackets ')'.

For example: input = "(first)and(second)" should return {0:6, 10:17}

If brackets cannot be paired or if the order is invalid (e.g. ')(')
return False. In this kata we care only about the positions of round brackets
'()', other types of brackets should be ignored.


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
