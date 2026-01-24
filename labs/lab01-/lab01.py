# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def factorial(n):
    """Return the factorial of a non-negative integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    return n * factorial(n-1)

def is_right_triangle(a, b, c):
    """Given three integers (maybe non-positive), judge whether the three
    integers can form the three sides of a right triangle.

    >>> is_right_triangle(2, 1, 3)
    False
    >>> is_right_triangle(5, -3, 4)
    False
    >>> is_right_triangle(5, 3, 4)
    True
    """
    "*** YOUR CODE HERE ***"
    m = max(a,b,c)
    return (2*m**2 == a**2 + b**2 + c**2)

def number_of_k(n, k):
    """Return the number of occurrences of k in each digit of a non-negative
    integer n.

    >>> number_of_k(999, 9)
    3
    >>> number_of_k(1234321, 2)
    2
    """
    "*** YOUR CODE HERE ***"
    n1 = n
    cnt = 0
    while (n1):
        if (n1 % 10 == k):
            cnt += 1
        n1 /= 10
    return cnt