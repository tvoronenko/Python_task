'''
Given an array arr containing only the characters 'R' (red), 'W' (white), and 'B' (blue), sort the array in-place so that the same colors are adjacent, with the colors in the order red, white, and blue.


Example 1:
Input: arr = ['R', 'W', 'B', 'B', 'W', 'R', 'W']
Output: ['R', 'R', 'W', 'W', 'W', 'B', 'B']
Explanation: All reds come first, then whites, then blues.

Example 2:
Input: arr = ['B', 'B', 'B', 'W', 'W', 'R', 'R', 'R']
Output: ['R', 'R', 'R', 'W', 'W', 'B', 'B', 'B']
Explanation: The colors are grouped and ordered correctly.

Example 3:
Input: arr = ['W', 'R']
Output: ['R', 'W']
Explanation: Red comes before white in the required ordering.
Constraints:

0 ≤ arr.length ≤ 10^5
arr[i] is either 'R', 'W', or 'B'

'''