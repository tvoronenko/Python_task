class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    cur = head
    prev = None
    while cur:
        tmp = cur.next
        cur.next = prev
        prev= cur
        cur = tmp

    return prev


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next = b
b.next = c
c.next = d

print(a.next.value)
print(b.next.value)
print(c.next.value)

reverse(a)

print(d.next.value)
print(c.next.value)
print(b.next.value)