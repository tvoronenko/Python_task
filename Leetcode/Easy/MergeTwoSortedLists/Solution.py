#complexity time O(m+n)
#space complexity O(m+n)
from Leetcode.DS.LinkedList.LinkedList import LinkedList
from Leetcode.DS.LinkedList.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1, l2) :
        # return another list if one is empty
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l3=None
        # go thru lists ntil they are nor empty
        while l1 and l2:
            if l1.val < l2.val:
                new_node=ListNode(l1.val)
                l1=l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next
            # if output list in not empty add another node and move to next
            if l3:
                l3.next = new_node
                l3 = l3.next
            # if output list is empty create head
            else:
                l3 = new_node
                head = l3
        # add remaining of list
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return head



if __name__ == '__main__':
    # begin
    s = Solution()
    l1 = LinkedList([1, 3,4])
    l2 = LinkedList([1, 2, 5])
    l3 = LinkedList([1, 1,2,3, 4,5])
    assert s.mergeTwoLists(l1.head,l2.head) == l3.head
    l1 = LinkedList([])
    l2 = LinkedList([])
    l3 = LinkedList([])
    assert s.mergeTwoLists(l1.head,l2.head) == l3.head
    l2 = LinkedList([0])
    l3 = LinkedList([0])
    assert s.mergeTwoLists(l1.head,l2.head) == l3.head