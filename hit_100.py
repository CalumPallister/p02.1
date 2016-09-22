"""
Problem:

     A game is played by trying to score exactly 100 points.
     The function hit_100 takes in a number of points. If the score is
     100, it should print "Winner!". For scores over 100, it should
     print "Too high", and for scores under 100 it should print "Too low"

Tests:

    >>> hit_100(72)
    Too low
    >>> hit_100(135)
    Too high
    >>> hit_100(100)
    Winner!

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def hit_100(score):

    if score < 100:
        print("Too low")

    elif score > 100:
        print("Too high")

    else:
        print("Winner!")
