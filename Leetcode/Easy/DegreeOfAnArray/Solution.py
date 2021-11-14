#complexity time O()
#space complexity O()
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left,right,count = {},{},{}
        # count frequency, left and most right position of each number
        for i,num in enumerate(nums):
            # left need to update only if empty for number
            if num not in left:
                left[num] = i
            # right need to update every time when we see number in array
            right[num] = i
            count[num] = count.get(num,0) + 1

        output = len(nums)
        # count degree
        degree = max(count.values())
        # select mininum subarray for elements with amount = degree
        for x in count:
            if count[x] == degree:
                output = min(output,right[x] - left [x] + 1)
        return output


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.findShortestSubArray([1,2,2,3,1]) == 2
    assert s.findShortestSubArray([1,2,2,3,1,4,2]) == 6

