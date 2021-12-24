#complexity time O()
#space complexity O()
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2
        for i in range(3,n+1):
            prev,curr = curr,prev + curr
        return curr



if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(5) == 8

