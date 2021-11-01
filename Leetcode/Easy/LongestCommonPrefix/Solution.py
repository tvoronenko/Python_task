#complexity time O(n*k) k - lengh of prefix, n - lengh of array strs
#space complexity O(1)
import math
class Solution:
    def longestCommonPrefix(self, strs):
        # find minimum lengh str, prefix will the same of less
        min_len = len(min(strs))
        if min_len == 0:
            return ""
        for i in range(min_len):
            ch = strs[0][i]
            # go thru all string and check i-th symbol
            for str in strs:
                if str[i] != ch:
                    return str[:i]
        return strs[0][:min_len]


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""