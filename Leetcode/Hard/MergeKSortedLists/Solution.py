#complexity time O()
#space complexity O()

class Solution:
    def mergeKLists(self, lists):
        pass


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.mergeKLists([[1,4,5],[1,3,4],[2,6]]) == [1,1,2,3,4,4,5,6]
    assert s.mergeKLists([[]]) == []