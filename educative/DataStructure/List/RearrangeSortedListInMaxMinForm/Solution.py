#complexity time O()
#space complexity O()
from typing import List

class Solution:
    def max_min(self,lst):
        result = []
        n=len(lst)
        for i in range(n//2):
            result.append(lst[-(i+1)])
            result.append(lst[i])
        if n % 2 == 1:
            result.append(lst[n//2])
        return result




if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.max_min([1, 2, 3, 4, 5, 6]) == [6,1,5,2,4,3]
    assert s.max_min([1, 2, 3, 4, 5]) == [5,1,4,2,3]