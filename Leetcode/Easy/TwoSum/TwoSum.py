class Solution:
    def twoSum(self, nums, target):
        seen = {}
        # go thru array and add number to hash table and also check presence of remaining
        for i,num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining],i]
            else:
                seen[num] = i
        return []

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6)) #[1,2]
    print(s.twoSum([2,7,11,15], 9))  # [0,1]
    assert s.twoSum([3, 2, 4], 6) == [1,2]
    assert s.twoSum([2,7,11,15], 9) == [0,1]