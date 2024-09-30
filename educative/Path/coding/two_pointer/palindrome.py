'''
Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums
whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers
exist in the array. Otherwise, return FALSE.

Time: The time complexity is O(n), where n  is the number of characters in the string. However, our algorithm will only run
(n/2) times, since two pointers are traversing toward each other.
Space: The space complexity is O(1), since we use constant space to store two indexes.
'''
class Solution:
    def is_palindrome(self,s):
        first = 0
        last = len(s) - 1
        while last > first:
            if s[last] == s[first]:
                last = last - 1
                first = first + 1
            else:
                return False
        return True

if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.is_palindrome("kaYak") == True)
    assert (s.is_palindrome("hello") == False)
    assert (s.is_palindrome("RaCEACAR") == False)
    assert (s.is_palindrome("A") == True)
    assert (s.is_palindrome("ABCDABCD") == False)
'''
1. Clarification on Definition of Palindrome
Should the check be case-sensitive? For example, should "Racecar" be considered a palindrome?
Should spaces and punctuation be ignored? For instance, should "A man, a plan, a canal, Panama!" be considered a palindrome?
Are we only considering alphanumeric characters? Do we need to ignore special characters in the string?
2. Input Constraints
What is the expected range of the input string length? Are there any performance concerns with very long strings?
Can the input string be empty? Should the function return True or False for an empty string?
3. Return Format
What should the function return? Should it return a boolean (True/False), or should it also include the original string for context?
4. Performance Requirements
Is there a performance constraint? Should we aim for a specific time complexity? For example, a linear time solution is usually expected.
5. Unicode and Character Set
Are we only dealing with ASCII characters, or should the function handle Unicode characters as well? This could affect how the string is processed.
'''