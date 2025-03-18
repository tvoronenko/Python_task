'''
Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

Time: The time complexity is O(n), where n  is the number of characters in the string. However, our algorithm will only run
(n/2) times, since two pointers are traversing toward each other.
Space: The space complexity is O(1), since we use constant space to store two indexes.
'''
class Solution:
    def is_palindrome(self,s):
        left = 0
        right = len(s) - 1
        while left < right:
        # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers inward
            left += 1
            right -= 1

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
Questions:
1. Clarification on Definition of Palindrome
Should the check be case-sensitive? For example, should "Racecar" be considered a palindrome?
Should spaces and punctuation be ignored? For instance, should "A man, a plan, a canal, Panama!" be considered a palindrome?
 # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
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
Use unicodedata for Normalization:
# Normalize Unicode string to decompose accented characters
    s = unicodedata.normalize('NFKD', s)

Tests:
1. Basic Test Cases
# Single-word palindromes
assert is_palindrome("racecar") == True
assert is_palindrome("madam") == True
assert is_palindrome("hello") == False

# Multi-word palindromes with spaces and punctuation ignored
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("Was it a car or a cat I saw?") == True
assert is_palindrome("No lemon, no melon") == True

# Case-sensitive test_show.py
assert is_palindrome("Racecar") == True

2. Edge Cases
# Empty String
assert is_palindrome("") == True  # An empty string is considered a palindrome

Single Character
assert is_palindrome("a") == True  # Single characters are palindromes
assert is_palindrome("Z") == True

# Numbers
assert is_palindrome("12321") == True  # Numeric palindrome
assert is_palindrome("12345") == False

# Strings with Only Non-Alphanumeric Characters
assert is_palindrome("!!!!") == True  # Only special characters are considered palindromes
assert is_palindrome("@#$%^&") == True

# Spaces and Punctuation
assert is_palindrome("taco cat") == True
assert is_palindrome("!@#$%t@c@o#$%^c@a@t!@#") == True  # Palindrome with mixed characters
assert is_palindrome("  ") == True  # Whitespace-only strings are palindromes

3. Unicode Test Cases
# Accented Characters
assert is_palindrome("Éso no sé! Eso no sé.") == True  # Handles accents
assert is_palindrome("¿Acaso hubo búhos acá?") == True  # Spanish palindrome
assert is_palindrome("mañana") == False  # Accented non-palindrome

# Mixed Scripts
assert is_palindrome("Able , was I saw eLba") == True  # Mixed case palindrome
assert is_palindrome("あいいあ") == True  # Japanese palindrome
assert is_palindrome("你好世界") == False  # Non-palindrome in Chinese
assert is_palindrome("あいうえお") == False  # Non-palindrome in Japanese
# Emoji Support

assert is_palindrome("😀a😀") == True  # Palindrome with emojis
assert is_palindrome("😀ab😀") == False

4. Large Input Test Cases
# Long Palindrome
long_palindrome = "a" * 10**6  # 1 million 'a's
assert is_palindrome(long_palindrome) == True

long_non_palindrome = "a" * (10**6 - 1) + "b"
assert is_palindrome(long_non_palindrome) == False

# Mixed Large Palindrome
long_mixed_palindrome = "a" * 10**5 + "b" + "a" * 10**5  # 'a...b...a' with 200k 'a's
assert is_palindrome(long_mixed_palindrome) == True

5. Stress Test Cases
Very Large Input
very_large_input = "a" * 10**7  # 10 million 'a's
assert is_palindrome(very_large_input) == True

very_large_non_palindrome = "a" * (10**7 - 1) + "b"
assert is_palindrome(very_large_non_palindrome) == False

6. Additional Non-Palindrome Examples
# Non-Palindromes with Similar Prefixes and Suffixes
assert is_palindrome("abcdecba") == False  # Prefix/suffix match, but middle mismatches
assert is_palindrome("abcdedcbaa") == False

# Non-Palindromes with Mixed Cases
assert is_palindrome("RaceCar") == True  # Case-insensitive
assert is_palindrome("RaceCaR") == True
assert is_palindrome("RaceCaR!") == True  # With punctuation ignored

Key Coverage:
ASCII
Single-word and multi-word palindromes.
Case-insensitive comparisons.
Handling punctuation and whitespace.

Unicode
Accented characters and decomposed forms.
Mixed scripts (e.g., Japanese, Chinese).
Emojis and special characters.

Edge Cases
Empty strings.
Single characters.
Non-alphanumeric strings.

Stress Testing
Very long strings (up to millions of characters).
Mixed-character inputs at scale.
'''