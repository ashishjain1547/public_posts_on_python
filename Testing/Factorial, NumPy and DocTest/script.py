import numpy as np
import doctest 

def factorial(n):
    """
    Test for the factorial of 3 that should pass.
    >>> factorial(3)
    6

    Test for the factorial of 0 that should fail.
    >>> factorial(0)
    1
    """
    return np.arange(1, n+1).cumprod()[-1]


def isEven(n):
    """
    Test that would pass
    >>> isEven(10)
    True

    Test that would fail
    >>> isEven(9)
    True

    Test that would pass
    >>> isEven(9)
    False
    """
    rtn = n % 2

    return rtn == 0
    
doctest.testmod()