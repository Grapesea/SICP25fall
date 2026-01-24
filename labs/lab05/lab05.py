# ANSWER QUESTION wwpd

def takeWhile(t, p):
    """Take elements from t until p is not satisfied.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> list(takeWhile(s, lambda x: x == 10))
    [10]
    >>> s2 = iter([1, 1, 2, 3, 5, 8, 13])
    >>> list(takeWhile(s2, lambda x: x % 2 == 1))
    [1, 1]
    >>> s = iter(['a', '', 'b', '', 'c'])
    >>> list(takeWhile(s, lambda x: x != ''))
    ['a']
    >>> list(takeWhile(s, lambda x: x != ''))
    ['b']
    >>> next(s)
    'c'
    """
    "*** YOUR CODE HERE ***"


def backAndForth(t):
    """Yields and skips elements from iterator t, back and forth.

    >>> list(backAndForth(iter([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    [1, 4, 5, 6]
    >>> list(backAndForth(iter([1, 2, 2])))
    [1]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = backAndForth(naturals())
    >>> [next(m) for _ in range(9)]
    [0, 3, 4, 5, 10, 11, 12, 13, 14]
    """
    "*** YOUR CODE HERE ***"


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale(iter([1, 5, 2]), 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [0, 2, 4, 6, 8]
    """
    "*** YOUR CODE HERE ***"


def merge(a, b):
    """Merge two generators that are in increasing order and without duplicates.
    Return a generator that has all elements of both generators in increasing
    order and without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"


def make_vending_machine(product, price):
    """
    Create a vending machine for the given product and price.

    >>> restock, deposit, vend = make_vending_machine('SICP book', 10)
    >>> deposit(7)
    'Machine is out of stock.'
    >>> restock(2)
    2
    >>> deposit(7)
    7
    >>> vend()
    'Insufficient balance. Please deposit 3 yuan more.'
    >>> deposit(5)
    12
    >>> vend()
    'Here is your SICP book and 2 yuan change.'
    >>> deposit(10)
    10
    >>> vend()
    'Here is your SICP book.'
    >>> vend()
    'Machine is out of stock.'
    """
    "*** YOUR CODE HERE ***"
