#complexity time O(n^2)
#space complexity O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        res = ""
        # for every char, check extending string, extending string can be odd or even lengh
        for i in range(len(s)):
            odd= self.isPalindrome(s,i,i)
            even = self.isPalindrome(s,i,i+1)
            # select max between odd,even and prev. result
            res = max(res,odd,even, key=len)
        return res


    def isPalindrome(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.longestPalindrome("babad") == "bab"
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("ac") == "a"