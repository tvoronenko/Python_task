'''
Given two sorted arrays arr1 and arr2, merge them into a single sorted array. The merged array should include all elements from both input arrays in sorted order.


Example 1:
Input:
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 4]
Output: [1, 2, 3, 4, 4, 4, 5]
Explanation: All elements are merged in sorted order.

Example 2:
Input:
arr1 = [-1]
arr2 = []
Output: [-1]
Explanation: When one array is empty, the result is just the other array.

Example 3:
Input:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
Explanation: Elements from both arrays are interleaved in sorted order.
Constraints:

arr1 and arr2 are sorted in ascending order
0 ≤ arr1.length, arr2.length ≤ 10^5
-10^9 ≤ arr1[i], arr2[i] ≤ 10^9

'''