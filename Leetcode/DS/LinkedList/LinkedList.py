from Leetcode.DS.LinkedList.ListNode import ListNode
class LinkedList:
    def __init__(self,l):
        if len(l)>0:
            self.head = ListNode()
            self.head.val = l[0]
        else:
            self.head = None
        curr = self.head
        for i in range(1,len(l)):
            node = ListNode(l[i])
            curr.next = node
            curr = curr.next


    def __str__(self):
        curr = self.head
        output = []
        while curr:
            output.append(curr.val)
            curr = curr.next
        return str(output)

    def __eq__(self,other):
        return str(self)==str(other)
