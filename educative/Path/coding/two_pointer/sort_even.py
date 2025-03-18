'''
Given an array of integers arr, modify it in-place so that all even numbers come before all odd numbers. The relative order of even/odd numbers does not need to be maintained.


Example 1:
Input: arr = [1, 2, 3, 4, 5]
Output: [2, 4, 1, 3, 5]
Note: [4, 2, 3, 1, 5] would also be a valid answer.

Example 2:
Input: arr = [5, 1, 3, 1, 5]
Output: [5, 1, 3, 1, 5]
Note: Since there are no even numbers, the array remains unchanged.

Example 3:
Input: arr = [1, 3, 2, 4]
Output: [2, 4, 1, 3]
Note: Any arrangement where the even numbers (2, 4) come before the odd
numbers (1, 3) is valid.
Constraints:

The length of arr is at most 10^5
Each element in arr is an integer in the range [-10^9, 10^9]
'''