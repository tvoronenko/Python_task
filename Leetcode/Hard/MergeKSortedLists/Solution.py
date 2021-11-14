#complexity time O()
#space complexity O()
from Leetcode.DS.LinkedList.LinkedList import LinkedList


class Solution:
    def mergeKLists(self, lists):
        pass


if __name__ == '__main__':
    # begin
    s = Solution()
    l1 = LinkedList([1,4,5])
    l2 = LinkedList([1,3,4])
    l3 = LinkedList([2,6])
    l4 = LinkedList([1,1,2,3,4,4,5,6])
    assert s.mergeKLists([l1.head,l2.head,l3.head]) == l4.head
    l3 = LinkedList([])
    l4 = LinkedList([])
    assert s.mergeKLists([l3.head]) == l4.head