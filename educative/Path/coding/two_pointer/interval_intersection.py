'''
Given two lists of closed intervals arr1 and arr2 where each interval is a [start, end] pair of integers, return a list containing all the intersections between intervals from arr1 and intervals from arr2. Each list is sorted by start time.

An intersection of two intervals is the interval that contains all points that are in both intervals. If the intersection is empty, it should not be included in the result.


Example 1:
Input:
arr1 = [[0, 1], [4, 6], [7, 8]]
arr2 = [[2, 3], [5, 9], [10, 11]]
Output: [[5, 6], [7, 8]]
Explanation:
- [4, 6] from arr1 intersects with [5, 9] from arr2 to give [5, 6]
- [7, 8] from arr1 intersects with [5, 9] from arr2 to give [7, 8]

Example 2:
Input:
arr1 = [[2, 4], [5, 8]]
arr2 = [[3, 3], [4, 7]]
Output: [[3, 3], [4, 4], [5, 7]]
Explanation:
- [2, 4] intersects with [3, 3] to give [3, 3]
- [2, 4] intersects with [4, 7] to give [4, 4]
- [5, 8] intersects with [4, 7] to give [5, 7]

Example 3:
Input:
arr1 = [[1, 3]]
arr2 = [[2, 4]]
Output: [[2, 3]]
Explanation: The intervals overlap from 2 to 3.
Interval intersection problem 1
Constraints:

0 ≤ arr1.length, arr2.length ≤ 10^4
arr1[i].length = arr2[j].length = 2
-10^9 ≤ start ≤ end ≤ 10^9
Each list is sorted by start time

'''