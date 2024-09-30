'''
Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums
whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers
exist in the array. Otherwise, return FALSE.

Time: In the solution above, sorting the array takes
O(nlog(n)) and the nested loop takes O(n2) to find the triplet. Here,n is the number of elements in the
input array. Therefore, the total time complexity of this solution is O(nlog(n)+n2), which simplifies to
O(n2)
Space: Because we use the built-in Python function, sort(), so the space complexity of the provided solution is
O(n).

'''
class Solution:
    def find_sum_of_three(self, nums, target):
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum == target:
                    return True
                if currSum > target:
                    right = right - 1
                else:
                    left = left + 1

        return False

if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.find_sum_of_three( [1,-1,0] , -1) == False)
    assert (s.find_sum_of_three( [1,-1,0, 2] , 0) == True)
    assert (s.find_sum_of_three( [3,7,1,2,8,4,5] , 10) == True)
    assert (s.find_sum_of_three( [3,7,1,2,8,4,5] , 21) == False)
    assert (s.find_sum_of_three([-1,2,1,-4,5,-3] , -8) == True)
    assert (s.find_sum_of_three( [-1,2,1,-4,5,-3] , 0) == True)

'''
1. Clarifying Input Constraints
Are there any constraints on the size of the input array? This helps determine if a brute-force or more optimized 
solution is necessary.
Can the array contain duplicate numbers? This might affect how you handle the results.
Are the numbers in the array all integers, or could they include floats? This helps confirm that the problem is 
dealing with whole numbers only.
What is the expected range of numbers in the array? Are they small integers, large integers, or could they be negative?
2. Clarifying Output Expectations
If multiple triplets sum up to the target, do I return any of them or just a boolean TRUE/FALSE? This will 
clarify if you should return the actual triplet or just the existence of one.
Should the triplets be unique? Do you need to handle cases where the same triplet appears multiple times in 
different positions?
3. Edge Cases
What should I return if the array has fewer than three elements? In such a case, we can't find a triplet, 
so it’s good to clarify how to handle this.
How should I handle cases where the array contains negative numbers? Although negative numbers are usually 
valid, confirming this can avoid surprises.
4. Performance Requirements
Are there any time or space complexity constraints? For example, do they expect an optimized solution (O(n²) 
with sorting) or is a brute-force O(n³) solution acceptable?
5. Input Format
Will the array always be non-empty, or should I account for an empty array? Just to clarify how you handle edge cases.
'''