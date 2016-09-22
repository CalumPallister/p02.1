"""
Problem:

    On the TV show, University Challenge, teams compete against each other
    to answer as many questions as possible correctly, which gives each
    team points. The winner always progress to the next round. However,
    a few losers also go through if they score enough points, in this case
    120.

    The function challenge takes in the scores of both teams.
    If team1 wins -> print "Team 1 progresses"
    If team2 wins -> print "Team 2 progresses"
    However, if the losing team scores 120 points or more, or there is a
    draw, instead print: "Both teams progress"

Tests:

    >>> challenge(110, 85)
    Team 1 progresses
    >>> challenge(90, 140)
    Team 2 progresses
    >>> challenge(135, 125)
    Both teams progress
    >>> challenge(105, 105)
    Both teams progress

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def challenge(team1, team2):

    if team1 > team2 and team2 < 120:
        print("Team 1 progresses")

    elif team2 > team1 and team1 < 120:
        print("Team 2 progresses")

    elif team1 == team2:
        print("Both teams progress")

    else:
        print("Both teams progress")
