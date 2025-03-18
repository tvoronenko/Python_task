'''
Given an array of integers, arr, where the length, n, is even, return whether the following condition holds for every k in the range 1 ≤ k <= n/2: "the sum of the first k elements is smaller than the sum of the first 2k elements." If this condition is false for any k in the range, return false.

Example 1: arr = [1, 2, 2, -1]
Output: True. The prefix [1] has a smaller sum than the prefix [1, 2], and the
prefix [1, 2] has a smaller sum than the prefix [1, 2, 2, -1]. The other
prefixes have length > n/2.

Example 2: arr = [1, 2, -2, 1, 3, 5]
Output: False. The prefix [1, 2] has a larger sum than the prefix [1, 2, -2,
1].
Constraints:

len(arr) is even
0 ≤ len(arr) ≤ 10^6
-10^9 ≤ arr[i] ≤ 10^9

'''