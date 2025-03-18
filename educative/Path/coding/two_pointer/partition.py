'''
Given an array arr and a pivot value, modify the array in-place to partition it into three sections:

Elements less than pivot
Elements equal to pivot
Elements greater than pivot
The relative order of elements within each section does not matter.


Example 1:
Input: arr = [1, 7, 2, 3, 3, 5, 3], pivot = 4
Output: [1, 2, 3, 3, 3, 7, 5]
Explanation: The array is partitioned into:
- Elements less than 4: [1, 2, 3, 3, 3]
- Elements equal to 4: []
- Elements greater than 4: [7, 5]

Example 2:
Input: arr = [1, 7, 2, 3, 3, 5, 3], pivot = 3
Output: [1, 2, 3, 3, 3, 7, 5]
Explanation: The array is partitioned into:
- Elements less than 3: [1, 2]
- Elements equal to 3: [3, 3, 3]
- Elements greater than 3: [7, 5]

Example 3:
Input: arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3], pivot = 4
Output: [3, 1, 2, 1, 3, 9, 5, 6, 5, 4]
Explanation: The array is partitioned into three sections around pivot 4.
Constraints:

0 ≤ arr.length ≤ 10^5
-10^9 ≤ arr[i], pivot ≤ 10^9

'''