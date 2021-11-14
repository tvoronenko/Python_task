#complexity time O()
#space complexity O()
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,l,r,type):
            while l<= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    while (mid >=l and mid <=r) and nums[mid] == target:
                        if type == 0:
                            mid -= 1
                        else:
                            mid += 1

                    if type == 0:
                        return mid + 1
                    else:
                        return mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                    return binary_search(nums,mid+1,r,type)
                else:
                    r =  mid - 1

            return -1


        first = binary_search(nums,0,len(nums) - 1,0)
        last = binary_search(nums, 0, len(nums) - 1,1)
        return [first,last]

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.searchRange([5,7,7,8,8,10],8) == [3,4]
    assert s.searchRange([5,7,7,8,8,10],6) == [-1,-1]
    assert s.searchRange([], 6) == [-1, -1]
    assert s.searchRange([1], 1) == [0, 0]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 5) == [0,0]