'''
You are given an array of letters, arr, and a string, word. We know that word appears within arr as a subsequence (its letters appear in order, though not necessarily contiguously). Identify the earliest occurrence of word in arr (that is, the first subsequence from left to right that spells out word) and move all those letters, in order, to the end of arr. You must do this in place, using only O(1) extra space, and preserve the relative order of both the moved letters and the remaining letters.


Example:	arr = [s, e, e, k, e, r, a, n, d, w, r, i, t, e, r], word = "edit"
Output:	[s, e, k, e, r, a, n, w, r, e, r, e, d, i, t]

The subsequence that needs to be moved is:

    [s, e, e, k, e, r, a, n, d, w, r, i, t, e, r]
        ^                    ^        ^  ^

Example:	arr = [b, a, c, b], word = "ab"
Output:	[b, c, a, b]. We cannot move the first 'b' because we need to find 'a'
first. [c, b, a, b] would be incorrect.

Example:	arr = [b, a, b, c], word = "b"
Output:	[a, b, c, b]. We must move the first 'b' to the end, not the second
one. [b, a, c, b] would be incorrect.
Constraints:

0 ≤ arr.length ≤ 10^5
0 ≤ word.length ≤ arr.length
arr and word contain only lowercase English letters

'''