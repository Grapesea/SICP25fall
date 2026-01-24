""" Homework 1: Variables & Functions, Control """

from operator import add, sub, mul, neg
from utils import *

def a_add_abs_b(a, b):
    r"""Return `a + abs(b)`, but without calling abs.

    >>> a_add_abs_b(2, 3)
    5
    >>> a_add_abs_b(2, -3)
    5
    >>> # a check to ensure that the return statement remains unchanged!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_add_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two largest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    >>> check_single_return(two_of_three)
    >>> check_no_square_brackets(two_of_three)
    """
    return x**2 + y**2 + z**2 - min(x,y,z)**2

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    res = 1
    for i in range(2, x//2):
        if (x % i == 0):
            res = x // i
            return res
    return res

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return False

def t():
    print(1)

def f():
    print(2)

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    a = x
    print(a)
    len = 1
    while (a != 1):
        if (a % 2 == 0):
            a = a // 2
        else:
            a = 3*a + 1
        print(a)
        len+=1
    return len

def double_factorial(n):
    """Compute the double factorial of n.

    >>> double_factorial(6)  # 6 * 4 * 2
    48
    >>> double_factorial(5)  # 5 * 3 * 1
    15
    >>> double_factorial(3)  # 3 * 1
    3
    >>> double_factorial(1)  # 1
    1
    """
    x = n
    m = n
    while x>2:
        x-=2
        m*=x
    return m
        
def double_ones(n):
    """Return true if n has two ones in a row.

    >>> double_ones(1)
    False
    >>> double_ones(11)
    True
    >>> double_ones(2112)
    True
    >>> double_ones(110011)
    True
    >>> double_ones(12345)
    False
    >>> double_ones(10101010)
    False
    """
    cnt = 0
    x = n

    while(x):    
        if(x%100 == 11):
            return True
        x = x // 10

    return False

def remove_even_position(n):
    """Removes the digits of n in even positions (the 2nd, 4th, 6th, … from left to right),
    and returns the number formed by the remaining digits.

    >>> remove_even_position(0)
    0
    >>> remove_even_position(10)
    1
    >>> remove_even_position(123)
    13
    >>> remove_even_position(123456)
    135
    """
    len = 0
    x = n
    
    while (x):
        len+=1
        x = x // 10
    if len <= 1:
        return n
    x = 0
    p = 0
    for p in range(0,len,2):
        bit = n // (10**(len-p-1)) % 10
        x = x*10 + bit
    
    return x

def second_largest(x, y, z):
    """Return the second largest value in `x`, `y`, and `z`.
    More precisely, if `x` is the second largest value in `x`, `y`, and `z`,
    then `y >= x >= z` or `z >= x >= y`.

    >>> second_largest(1, 1, 1)
    1
    >>> second_largest(1, 2, 3)
    2
    >>> second_largest(6, 5, 4)
    5
    >>> second_largest(1, 3, 2)
    2
    >>> second_largest(2, 3, 1)
    2
    >>> second_largest(2, 2, 1)
    2
    >>> second_largest(1, 2, 1)
    1
    >>> second_largest('a', 'b', 'c') # strings in python are also comparable
    'b'
    >>> check_no_square_brackets(second_largest)
    """
    if x >= y:
        if x <= z:
            return x
        else:
            return max(y,z)
    else:
        if x >= z:
            return x
        else:
            return min(y,z)