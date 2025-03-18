'''
Given a valley-shaped array, arr, return a new array with the elements sorted in ascending order. A valley-shaped array is an array of integers such that:

It can be split into a non-empty prefix and a non-empty suffix
The prefix is sorted in decreasing order (duplicates allowed)
The suffix is sorted in increasing order (duplicates allowed)

Example 1: arr = [8, 4, 2, 6]
Output:	[2, 4, 6, 8]

Example 2: arr = [1, 2]
Output:	[1, 2]. The array is already sorted (the prefix is just [1]).

Example 3: arr = [2, 2, 1, 1]
Output:	[1, 1, 2, 2]
Constraints:

0 ≤ arr.length ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9
'''