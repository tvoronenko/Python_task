'''
Given an array arr, modify it in-place by moving the first third of the elements to the end while keeping the relative order of elements within each third. The array length will be divisible by 3.


Example 1:
Input: arr = ['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']
Output: ['r', 'e', 'v', 'i', 'e', 'w', 'b', 'a', 'd']
Explanation: The first third (bad) moves to the end, while the rest (review)
stays in order.

Example 2:
Input: arr = ['a', 'b', 'c']
Output: ['b', 'c', 'a']
Explanation: The first element 'a' moves to the end.

Example 3:
Input: arr = []
Output: []
Explanation: Empty array remains empty.
Constraints:

The length of arr is divisible by 3
0 ≤ arr.length ≤ 10^5

'''