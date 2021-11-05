#complexity time O(log 10 (n))
#space complexity O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x > 0 and x % 10 == 0):
            return False
        remain = 0
        while x > remain:
            remain = remain * 10 + x % 10
            x = x // 10
        if (x==remain) or (x==remain // 10):
            return True
        else:
            return False

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-10) == False
    assert s.isPalindrome(10) == False
    assert s.isPalindrome(2332) == True