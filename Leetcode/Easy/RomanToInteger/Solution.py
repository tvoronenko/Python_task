#complexity time O(n)
#space complexity O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        i = len(s) - 1
        while i >= 1:
            if dict_number[s[i]] <= dict_number[s[i-1]]:
                number = number + dict_number[s[i]]
                i -= 1
            else :
                number = number + dict_number[s[i]] - dict_number[s[i-1]]
                i -= 2

        if i==0:
            number = number + dict_number[s[0]]
        return number



if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994