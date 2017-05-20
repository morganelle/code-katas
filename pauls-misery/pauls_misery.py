"""

Kata: Paul's Misery

#1 Best Practices Solution by CrazyMerlyn
def paul(x):
    points = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
    misery = sum(map(points.get, x))
    return ['Miserable!', 'Sad!', 'Happy!', 'Super happy!']\
            [(misery<40)+(misery<70)+(misery<100)]

Instructions
----------------------------------------------------------------------
Paul is an excellent coder and sits high on the CW leaderboard. He
solves kata like a banshee but would also like to lead a normal life,
with other activities. But he just can't stop solving all the kata!!

Given an array (x) you need to calculate the Paul Misery Score.
The values are worth the following points:

kata = 5 Petes kata = 10 life = 0 eating = 1

The Misery Score is the total points gained from the array.
Once you have the total, return as follows:

<40 = 'Super happy!'
<70 >=40 = 'Happy!'
<100 >=70 = 'Sad!'
>=100 = 'Miserable!'

"""


def paul(x):
    count = 0
    for word in x:
        if word == 'eating':
            count = count + 1
        elif word == 'kata':
            count = count + 5
        elif word == 'Petes kata':
            count = count + 10
    if count >= 100:
        return 'Miserable!'
    elif count < 100 and count >= 70:
        return 'Sad!'
    elif count < 70 and count >= 40:
        return 'Happy!'
    elif count < 40:
        return 'Super happy!'
