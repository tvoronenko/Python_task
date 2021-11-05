#complexity time O()
#space complexity O()

class Solution:
    def mergeTwoLists(self, l1, l2) :
        pass


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.mergeTwoLists([1,2,4], [1,3,4]) == [1,1,2,3,4,4]
    assert s.mergeTwoLists([],[]) == []
    assert s.mergeTwoLists([], [0]) == [0]