#complexity time O()
#space complexity O()
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            if num == 0: return 0
            product *= num
        if product > 0:
            return 1
        else:
            return -1


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.arraySign([-1,-2,-3,-4,3,2,1]) == 1
    assert s.arraySign([1,5,0,2,-3]) == 0
    assert s.arraySign( [-1,1,-1,1,-1]) == -1



    """There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product)."""