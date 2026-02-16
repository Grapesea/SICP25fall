""" Homework 07: Special Method, Linked Lists and Mutable Trees"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __add__(self, other):
        c = self.coefficients.copy() 
        # 第二次遇到这个问题了，需要仔细看是否为原处改动
        l1 = len(self.coefficients)
        l2 = len(other.coefficients)
        
        for i in range(min(l1,l2)):
            c[i] += other.coefficients[i]
        if l1 < l2:
            c.extend(other.coefficients[l1:])
        return Polynomial(c)

    def __mul__(self, other):        
        l1 = len(self.coefficients)
        l2 = len(other.coefficients)
        m = [0 for _ in range(l1 + l2 -1)]
        
        for i in range(len(m)): #计算i次幂的系数
            for j in range(max(i - l2 + 1, 0), min(l1 - 1, i) + 1): # 同时满足 0 <= j <= l1-1 && 0 <= i-j <= l2-1
                m[i] += (self.coefficients[j] * other.coefficients[i-j])
        n = Polynomial(m)   
        
        return n
    
    def __repr__(self):
        if len(self.coefficients) == 1:
            return f"Polynomial({self.coefficients})"
        
        while self.coefficients[-1] == 0:
            self.coefficients.pop()
        return f"Polynomial({self.coefficients})"
        
    def __str__(self):
        m = self.coefficients
        res = ""
        if len(m) == 1:
            return f"{m[0]}"
        
        elif len(m) == 2:
            res = ""
            if m[1] > 0:
                res += f"{m[1]}x "
            elif m[1] < 0:
                res += f" - {abs(m[1])}x "
            if m[0] > 0:
                res += f" + {m[0]}"
            elif m[0] < 0:
                res += f"+ {m[0]}"
            else:
                res += "0"
        else:
            for i in range(len(m)):
                if m[i] == 0:
                    if i == 0:
                        res += f"0"
                    else:
                        res += f" + 0*x^{i}"
                else:
                    if i == 0:
                        res += f"{m[i]}"
                    else:
                        res += f" + {m[i]}*x^{i}"
        return res



def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    # 刚开始我就有个疑惑，这个题要考虑 Link(1, Link(2, Link(1))) 这种情况吗，但这个违反了sorted原则.
    
    if lnk.rest is Link.empty:
        return
    if lnk.rest.first == lnk.first:
        lnk.rest = lnk.rest.rest # 保留first节点
        remove_duplicates(lnk) # 这里是考虑到样例中的多重重复，所以接着检查当前节点
    else:
        remove_duplicates(lnk.rest) # 继续考虑子问题

def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    rst = reverse(lnk.rest) # 获得新的“头指针”，也就是最后一个值
    
    lnk.rest.rest = lnk
    lnk.rest = Link.empty # 反转指针指向
    return rst
    
def rotate_right(lnk):
    """Rotate the linked list one step to the right.

    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> # Disallow creating new Links
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = rotate_right(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <4 1 2 3>
    >>> a.first   # Make sure original first not overwritten
    1
    """
    p = lnk
    p_prev = lnk
    while p.rest is not Link.empty:
        p_prev = p
        p = p.rest
    p_prev.rest = Link.empty
    p.rest = lnk
    return p

    # 折腾了很久C++，刚开始看这种结构实现觉得很奇怪，但实质上是一样的.

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self, other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        
        if self.label != other.label:
            return False
        if len(self.branches) != len(other.branches):
            return False
        for b in range(len(self.branches)):
            if not Tree.__eq__(self.branches[b], other.branches[b]):
                return False
        return True
        
        
        
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    def bst_min(t):
        if Tree.is_leaf(t):
            return t.label
        return bst_min(t.branches[0])
    
    def bst_max(t):
        if Tree.is_leaf(t):
            return t.label
        if len(t.branches) == 1:
            return bst_max(t.branches[0])
        if len(t.branches) == 2:
            return bst_max(t.branches[1])
    
    if len(t.branches) > 2:
        return False
    if not Tree.is_leaf(t):
        if len(t.branches) == 2:
            if t.branches[1].label <= t.label or t.branches[0].label > t.label:
                return False
        if len(t.branches) == 2:
            if bst_min(t.branches[0]) > t.label:
                return False
            if bst_max(t.branches[1]) < t.label:
                return False
        
        for b in t.branches:
            if not is_bst(b):
                return False
    return True


def count_coins(total, denominations):
    """
    Given a positive integer `total`, and a list of denominations,
    a group of coins make change for `total` if the sum of them is `total` 
    and each coin is an element in `denominations`.
    The function `count_coins` returns the number of such groups. 
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(total, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since there is no way to make change with empty denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    if total == 0:
        return Tree("1")
    if total < 0:
        return None
    if len(denominations) == 0:
        return None
    
    without_current = count_coins_tree(total, denominations[1:])
    with_current = count_coins_tree(total - denominations[0], denominations)
    
    b = []
    if without_current is not None:
        b.append(without_current)
    if with_current is not None:
        b.append(with_current)
    
    if len(b) == 0:
        return None
    l = f"{total}, {denominations}" # 输出结果看起来很长，实则是字符串构成的Tree节点label
    return Tree(l, b)


##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    def is_cycle(lnk): #因为成环只可能在链表的末尾，所以可以写一个辅助的判断函数.
        if lnk is Link.empty:
            return False
        if lnk.rest is Link.empty:
            return False
        
        f = lnk.rest
        while f.rest:
            f = f.rest
            if f == lnk:
                return True
        return False
    
    if lnk.rest is Link.empty:
        return False
    p = lnk.rest
    
    while p.rest is not Link.empty:
        p = p.rest
        if is_cycle(p):
            return True
    return False


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    def weight(t):
        if t.is_leaf():
            return t.label
        return t.label + sum(weight(b) for b in t.branches)
    
    if t.is_leaf():
        return
    for b in t.branches:
        balance_tree(b)
    b_w = [weight(b) for b in t.branches]
    max_bw = max(b_w)
    
    for i in range(len(b_w)):
        t.branches[i].label += (max_bw - b_w[i])
    

#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
