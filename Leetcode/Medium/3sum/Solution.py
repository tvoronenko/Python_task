#complexity time O(n^2)
#space complexity O(log n - n)

class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        k=0
        # i+j+k=0 it is the same i
        for i in range(len(nums)):
            # we have sorted array, if the first number is bigger than 0, so we cannot find ```triplet that equal 0
            if nums[i] > k:
                break
            # for avoiding duplicates
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result,k)
        return result

    def twoSum(self, nums, i, result,k):
        # we have sorted array, so it will be easy to use two pointer technique
        low = i + 1
        hi= len(nums) - 1
        while (low < hi):
            sum = nums[i] + nums[low] + nums[hi]
            #need to move to right because sum is less 0
            if sum < k:
                low += 1
            #need to move to left becasue sum is more than 0
            elif sum > k:
                hi -= 1
            #we found triplet, need to move both pointer
            else:
                result.append([nums[i], nums[low], nums[hi]])
                low += 1
                hi -= 1
                #for avoiding duplicates
                while low < hi and nums[low] == nums[low - 1]:
                    low += 1



if __name__ == '__main__':
    # begin
    s = Solution()
    print(search_triplets([-1,0,1,2,-1,-4]))
    #assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    #assert s.threeSum([]) == []
    #assert s.threeSum([0]) == []