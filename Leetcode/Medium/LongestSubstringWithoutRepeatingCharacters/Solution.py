#complexity time O(2n)
#space complexity O(min(m,n) m - alphabet

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left = 0
        right = 1
        window_len = 1
        counter = {s[left]:1}
        # go thru all string and use sliding window to find max substring with non repeat chars
        while right < len(s):
            # check if right bound in hash table and if yes check for repeating
            if s[right] in counter and counter[s[right]] > 0:
                counter[s[right]] += 1
                # if char if repeated move left bound until got thru repeated chars
                while counter[s[right]] > 1:
                    counter[s[left]] -=1
                    left += 1
            else:
                counter[s[right]] = 1
            # select max between old and current len of window
            window_len = max(window_len, right - left + 1)
            right += 1
        return window_len
# can be used instead of hash table
#chars = [0] * 128
#chars[ord(r)]+=1
#also can be optimized if store next index after last seen char

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0