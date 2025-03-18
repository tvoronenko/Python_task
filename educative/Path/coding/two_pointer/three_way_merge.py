'''
Given three sorted arrays arr1, arr2, and arr3, merge them into a single sorted array while removing any duplicates. The input arrays may contain duplicates, but each value should appear only once in the output array.


Example 1:
Input:
arr1 = [2, 3, 3, 4, 5, 7]
arr2 = [3, 3, 9]
arr3 = [3, 3, 9]
Output: [2, 3, 4, 5, 7, 9]
Explanation: The value 3 appears multiple times in the input but only once in
the output.

Example 2:
Input:
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [3, 4, 5]
Output: [1, 2, 3, 4, 5]
Explanation: Each duplicate value is included only once.

Example 3:
Input:
arr1 = [1, 1, 1]
arr2 = [1, 1]
arr3 = [1]
Output: [1]
Explanation: All ones are merged into a single occurrence.
Constraints:

The input arrays are sorted in ascending order
0 ≤ arr1.length, arr2.length, arr3.length ≤ 10^5
-10^9 ≤ arr1[i], arr2[i], arr3[i] ≤ 10^9
'''