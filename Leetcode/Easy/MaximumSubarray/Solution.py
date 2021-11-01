class Solution:
    def maxSubArray_brute(self, nums):
        max_sum = 0
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i,len(nums)):
                current_sum += nums[j]
                max_sum = max(current_sum, max_sum)
        return max_sum

    # complexity time O(n)
    # space complexity O(1)
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]
        for i in nums[1:]:
            # figure out what is better i or prev.sum + i
            current_sum = max(i, current_sum + i)
            # select max between current sum and prev sum
            max_sum = max(max_sum,current_sum)
        return max_sum

    # the same as above but more here formula is more understandable
    # complexity time O(n)
    # space complexity O(n)
    def maxSubArray_dp(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            max_sum = max(max_sum, dp[i])
        return max_sum

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5,4,-1,7,8]) == 23