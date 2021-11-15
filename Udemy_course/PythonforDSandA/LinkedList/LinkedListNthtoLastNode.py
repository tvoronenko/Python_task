class Node:

    def __init__(self, value):
        self.value = value
        self.next  = None

def nth_to_last_node(n, head):
    slow = head
    fast = head
    for _ in range(n):
        if fast:
            fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


####

class TestNLast(object):

    def test(self, sol):
        assert_equal(sol(2, a), d)
        print
        'ALL TEST CASES PASSED'


# Run tests
t = TestNLast()
t.test(nth_to_last_node)