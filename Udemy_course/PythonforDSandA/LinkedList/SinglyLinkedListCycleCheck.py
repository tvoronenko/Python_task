"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a  # Cycle Here!

# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z

f = Node(1)

d= Node(1)
e=Node(2)
d.next = e
e.next = d
#############
class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)
        assert_equal(sol(f), False)
        assert_equal(sol(d), True)

        print
        "ALL TEST CASES PASSED"


# Run Tests

t = TestCycleCheck()
t.test(cycle_check)