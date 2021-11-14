#complexity time O()
#space complexity O()
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_counter = defaultdict(int)
        for i in range(len(t)):
            dict_counter[s[i]] += 1
            dict_counter[t[i]] -= 1

        for i in dict_counter.values():
            if i != 0:
                return False
        return True




if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat","car") == False