'''Given a sorted array arr, remove all duplicates in-place and return the length of the array with duplicates removed. The first K elements of the array should contain the final result, where K is the returned length. The order of elements should be kept the same.

Note that you must do this by modifying the input array in-place with O(1) extra memory.


Example 1:
Input: arr = [1, 2, 2, 3, 3, 3, 5]
Output: 4
After the operation, the first 4 elements should be [1, 2, 3, 5]

Example 2:
Input: arr = []
Output: 0
After the operation, the array remains empty

Example 3:
Input: arr = [1, 1, 1]
Output: 1
After the operation, the first element should be [1]
Constraints:

The array is sorted in non-decreasing order
The length of arr is at most 10^5
Each element in arr is an integer'''