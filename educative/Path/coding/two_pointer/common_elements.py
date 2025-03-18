'''
Given two sorted arrays arr1 and arr2, find their intersection. The intersection should include all elements that appear in both arrays, including duplicates. The result should be returned in sorted order.


Example 1:
Input:
arr1 = [1, 2, 3]
arr2 = [1, 3, 5]
Output: [1, 3]
Explanation: 1 and 3 appear in both arrays.

Example 2:
Input:
arr1 = [1, 1, 1]
arr2 = [1, 1]
Output: [1, 1]
Explanation: Two 1s appear in both arrays.

Example 3:
Input:
arr1 = [1, 2, 2, 3]
arr2 = [2, 2, 3]
Output: [2, 2, 3]
Explanation: Two 2s and one 3 appear in both arrays.
Constraints:

The input arrays are sorted in ascending order
0 ≤ arr1.length, arr2.length ≤ 10^5
-10^9 ≤ arr1[i], arr2[i] ≤ 10^9
'''