"""Lab 3: Recursion"""

LAB_SOURCE_FILE = "lab03.py"


# ANSWER QUESTION q1

# ANSWER QUESTION q2

# ANSWER QUESTION q3


def number_of_k(n, k):
    """Return the number of occurrences of k in each digit of a non-negative
    integer n.

    >>> number_of_k(999, 9)
    3
    >>> number_of_k(1234321, 2)
    2
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'number_of_k', ['While', 'For'])
    True
    """
    return 0 if n < 10 and n != k else (n % 10 == k) + number_of_k(n//10, k) 


def f91(n):
    """Takes a number n and returns n - 10 when n > 100,
    returns f91(f91(n + 11)) when n ≤ 100.

    >>> f91(1)
    91
    >>> f91(2)
    91
    >>> f91(100)
    91
    """
    return n-10 if n > 100 else f91(f91(n + 1))


def is_monotone(n):
    """Returns whether n has monotone digits.
    Implement using recursion!

    >>> is_monotone(22000130)
    False
    >>> is_monotone(1234)
    True
    >>> is_monotone(24555)
    True
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'is_monotone', ['While', 'For'])
    True
    """
    return True if n < 10 else (n % 10 >= (n % 100 // 10)) and is_monotone(n // 10)


def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(10)
    89
    """
    return 1 if n <= 1 else count_stair_ways(n-1) + count_stair_ways(n-2)


def count_k(n, k):
    """Counts the number of paths to climb up a flight of n stairs,
    taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    >>> count_k(3, 5) # Take no more than 3 steps
    4
    """
    dp = [[0 for i in range (k+1)] for i in range(n+1)]
    for i in range(1,n+1):
        dp[i][1] = 1
    for i in range(1,k+1):
        dp[1][i] = 1
    for i in range(2,n+1):
        for j in range(2,k+1):
            dp[i][j] = dp[i][i] if i < j else (sum(dp[s][j] for s in range(1, i))+1 if i == j else sum([dp[i - step][j] for step in range(1, j + 1)]))
            # print(f"dp[{i}][{j}] = {dp[i][j]}")
    return dp[n][k]
    
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m-1,n) + paths(m,n-1)
    