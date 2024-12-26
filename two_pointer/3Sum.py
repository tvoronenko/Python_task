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
        if len(nums) < 3:
            return False
        
        if not nums:
            return False

        nums.sort()
        for i in range(len(nums)):
            # Skip duplicates for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
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
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

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
Questions: 

1. Clarifying Input Constraints
Are there any constraints on the size of the input array? This helps determine if a brute-force or more optimized 
solution is necessary.
Can the array contain duplicate numbers? This might affect how you handle the results.
Are the numbers in the array all integers, or could they include floats? This helps confirm that the problem is 
dealing with whole numbers only.  
epsilon = 1e-9  # Tolerance for floating-point comparison
if abs(current_sum - target) < epsilon:  # Use tolerance for equality
    return True
What is the expected range of numbers in the array? Are they small integers, large integers, or could they be negative?
2. Clarifying Output Expectations
If multiple triplets sum up to the target, do I return any of them or just a boolean TRUE/FALSE? This will 
clarify if you should return the actual triplet or just the existence of one.
Should the triplets be unique? Do you need to handle cases where the same triplet appears multiple times in 
different positions?
3. Edge Cases
What should I return if the array has fewer than three elements? In such a case, we can't find a triplet, 
so it’s good to clarify how to handle this.
Are there specific edge cases I should consider, such as all negative numbers, all zeros, or a mix of positive and negative numbers?
Although negative numbers are usually valid, confirming this can avoid surprises.
4. Performance Requirements
Are there any time or space complexity constraints? For example, do they expect an optimized solution (O(n²) 
with sorting) or is a brute-force O(n³) solution acceptable?
5. Input Format
Will the array always be non-empty, or should I account for an empty array? 
What should I do if the input is invalid (e.g., non-integer elements or fewer than three integers)? 
Just to clarify how you handle edge cases.

Tests:
1. Basic Test Cases
Triplet Exists:
assert three_sum_exists([1, 2, 3, 4, 5], 9) == True  # 1 + 3 + 5 = 9
assert three_sum_exists([-1, 0, 1, 2, -1, -4], 0) == True  # -1 + 0 + 1 = 0

Triplet Does Not Exist:
assert three_sum_exists([1, 2, 3, 4], 50) == False  # No triplet sums to 50
assert three_sum_exists([-5, -3, -1, 0], 1) == False  # No positive sum possible

2. Edge Cases
Smallest Valid Input:
Copy code
assert three_sum_exists([1, 1, 1], 3) == True  # The only three numbers sum to 3

All Negative Numbers:
assert three_sum_exists([-8, -5, -3, -1], -9) == True  # -5 + -3 + -1 = -9
assert three_sum_exists([-8, -5, -3, -1], 0) == False  # No sum reaches 0

All Positive Numbers:
assert three_sum_exists([5, 7, 10, 12], 22) == True  # 5 + 7 + 10 = 22
assert three_sum_exists([5, 7, 10, 12], 50) == False  # No triplet sums to 50

Array with Zeros:
assert three_sum_exists([0, 0, 0, 0], 0) == True  # 0 + 0 + 0 = 0
assert three_sum_exists([0, 0, 0, 1], 3) == False  # No triplet sums to 3

All Identical Numbers
Test arrays where all numbers are the same.
assert three_sum_exists([2, 2, 2, 2], 6) == True  # 2 + 2 + 2 = 6
assert three_sum_exists([2, 2, 2, 2], 7) == False  # No triplet sums to 7

Large Negative Target
Arrays with a mix of positive and negative numbers, and a large negative target.
assert three_sum_exists([-10, -20, -30, 5, 10], -50) == True  # -20 + -30 + 5 = -50
assert three_sum_exists([-10, -20, -30, 5, 10], -100) == False  # No triplet sums to -100

Mix of Large and Small Numbers
Test arrays with widely varying magnitudes.
assert three_sum_exists([1000000, -1000000, 1, 2, 3], 3) == True  # 1 + 2 + 3 = 3
assert three_sum_exists([1000000, -1000000, 1, 2, 3], 100) == False  # No triplet sums to 100

Floating-Point Numbers
If the problem allows floating-point values, test for precision handling.
assert three_sum_exists([1.1, 2.2, 3.3, 4.4], 6.6) == True  # 1.1 + 2.2 + 3.3 = 6.6
assert three_sum_exists([1.1, 2.2, 3.3, 4.4], 7.0) == False  # No triplet sums to 7.0

3. Stress Test Cases
Large Array:
large_array = list(range(1, 10000))
assert three_sum_exists(large_array, 15) == True  # Example: 1 + 5 + 9 = 15
assert three_sum_exists(large_array, 30000) == False  # No valid triplet

Duplicate Numbers:
assert three_sum_exists([1, 1, 2, 2, 3, 3], 6) == True  # 1 + 2 + 3 = 6
assert three_sum_exists([1, 1, 2, 2, 3, 3], 10) == False  # No valid triplet

4. Performance Tests
Very Large Array with Small Target
Test how the function handles large arrays with small targets.
large_array = list(range(-500, 500))  # Numbers from -500 to 499
assert three_sum_exists(large_array, 0) == True  # -1 + 0 + 1 = 0
assert three_sum_exists(large_array, 1500) == False  # No triplet sums to 1500

All Zeros
Large array with all elements being zero.
assert three_sum_exists([0] * 10000, 0) == True  # 0 + 0 + 0 = 0
assert three_sum_exists([0] * 10000, 1) == False  # No triplet sums to 1
'''