#complexity time O(n)
#space complexity O(n)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalidrome(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
            else:
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalidrome(s,i,j-1) or isPalidrome(s,i+1,j)
            else:
                i += 1
                j -= 1
        return True

    # Time: O(n)
    # Space: O(n)
    def validPalindrome_more_effic(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.validPalindrome("aba") == True
    assert s.validPalindrome("abca") == True
    assert s.validPalindrome("abc") == False