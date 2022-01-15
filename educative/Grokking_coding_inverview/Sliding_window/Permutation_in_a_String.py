'''
Given a string and a pattern, find out if the string contains any permutation of the pattern
Time: O(N+M)
Space: O(M)
'''
from collections import Counter


def find_permutation(str, pattern):
    window_start, matched = 0, 0
    window_end = 0
    char_frequency = Counter(pattern)
    # our goal is to match all the characters from the 'char_frequency' with the current window
    while window_end < len(str):
        right = str[window_end]
        if right in char_frequency:
            char_frequency[right] -= 1
            if char_frequency[right] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True

        if window_end >= len(pattern) - 1:
            left = str[window_start]
            if left in char_frequency:
                if char_frequency[left] == 0:
                    matched -= 1
                char_frequency[left] += 1
            window_start += 1
        window_end += 1

    return False


def main():
    print(find_permutation("oidbcaf","abc")) #true
    print(find_permutation("odicf", "dc"))  # false
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))  # true
    print(find_permutation("aaacb", "abc"))  # true


main()