"""
Problem:

    The function factor_test takes in two numbers, a and b.
    If a and b are the same - print "a = b"
    If a is a factor of b - print "a is a factor of b"
    If b is a factor of a - print "b is a factor of a"
    Otherwise, print "No factors here"

Tests:

    >>> factor_test(10, 5)
    b is a factor of a
    >>> factor_test(23, 23)
    a = b
    >>> factor_test(9, 11)
    No factors here
    >>> factor_test(7, 28)
    a is a factor of b

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this function
def factor_test(a, b):

    if a == b:
        print("a = b")

    elif a % b == 0:
        print("b is a factor of a")

    elif b % a == 0:
        print("a is a factor of b")

    else: print("No factors here")
