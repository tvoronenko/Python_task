#complexity time O()
#space complexity O()
from typing import List

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        # create group of 0's and 1's
        for i in range(1, len(s)):
            # if bit is switched starting new group
            if s[i - 1] != s[i]:
                groups.append(1)
            # if bit is the same increasing last group
            else:
                groups[-1] += 1

        ans = 0
        # count amount of group, by selecting minimun of 0 or 1 in groups
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.countBinarySubstrings("00110011") == 6
    assert s.countBinarySubstrings("10101") == 4