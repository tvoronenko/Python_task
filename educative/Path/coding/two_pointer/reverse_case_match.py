'''
Given a string s containing both uppercase and lowercase letters, determine if the lowercase letters match the uppercase letters in reverse order. In other words, check if the sequence of lowercase letters matches the sequence of uppercase letters when read backwards.


Example 1:
Input: s = "haDrRAHd"
Output: true
Explanation:
- Lowercase letters: "hard"
- Uppercase letters: "DRAH"
- When reversed, "DRAH" becomes "HARD", which matches "hard" ignoring case.

Example 2:
Input: s = "haHrARDd"
Output: false
Explanation:
- Lowercase letters: "hard"
- Uppercase letters: "HARD"
- When reversed, "HARD" becomes "DRAH", which doesn't match "hard".

Example 3:
Input: s = "BbbB"
Output: true
Explanation:
- Lowercase letters: "bb"
- Uppercase letters: "BB"
- When reversed, "BB" becomes "BB", which matches "bb" ignoring case.
Constraints:

0 ≤ s.length ≤ 10^5
s contains only uppercase and lowercase English letters
'''