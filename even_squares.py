"""
Problem:

    The function even_squares takes in a number. If the number is:
    * even - print out the number squared
    * odd - print out the number

Tests:

    >>> even_squares(20)
    400
    >>> even_squares(9)
    9
    >>> even_squares(8)
    64
    >>> even_squares(73)
    73
"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def even_squares(n):

    if n % 2 == 0:
        print(n * n)

    else:
        print(n)
