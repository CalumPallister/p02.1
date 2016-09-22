"""
Problem:

    The function biggest takes in three variables: a, b and c.
    It should print out the biggest of the three.

Tests:

    >>> biggest(10, 12, 7)
    12
    >>> biggest(27, 16, 22)
    27
    >>> biggest(15, 11, 19)
    19
    >>> biggest(11, 6, 11)
    11

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def biggest(a, b, c):

    if a > b and a > c and not a == b or a == c:
        print(a)

    elif b > c and b > a and not b == c or b == a:
        print(b)

    elif c > a and c > b and not c == a or c == b:
        print(c)

    elif a == c:
        print((a + c) // 2)
