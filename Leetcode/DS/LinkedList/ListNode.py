class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next
        return str(output)

    def __eq__(self, other):
        return str(self) == str(other)