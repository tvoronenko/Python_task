#complexity time O(n)
#space complexity O(1)

from Leetcode.DS.LinkedList.LinkedList import LinkedList

class Solution:
    def removeNthFromEnd(self, head, n) :
        if head.next is None:
            return None
        fast = head
        slow = head
        # move fast in n position ahead. We don't need to chesk that fast is exist, because n is equal or less lengh of linked list
        for i in range(n):
            fast = fast.next
        # if fast is end of linked list that mean we need to remove first item, just return head.next
        if fast is None:
            return head.next
        # now move two pointer until fast reach end, and every time difference between slow and fast will be n
        while fast.next:
            fast = fast.next
            slow = slow.next
        # element  after slow is element that need to remove, just change link to next.next instead of next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    # begin
    s = Solution()
    #1
    l=LinkedList([1,2,3,4,5])
    l2=LinkedList([1,2,3,5])
    actual_result=s.removeNthFromEnd(l.head,2)
    assert actual_result == l2.head
    #2
    l = LinkedList([1])
    l2 = LinkedList([])
    actual_result = s.removeNthFromEnd(l.head, 1)
    assert actual_result == l2.head
    #3
    l = LinkedList([1,2])
    l2 = LinkedList([1])
    actual_result = s.removeNthFromEnd(l.head, 1)
    assert actual_result == l2.head