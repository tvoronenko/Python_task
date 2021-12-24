'''
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Time: O(n)
Space: O(k)
'''
import math


def longest_substring_with_k_distinct(str1, k):
  max_len = 0
  start = 0
  end = 0
  dict_count = {}
  # in the following loop we'll try to extend the range [window_start, window_end]
  while end < len(str1):
        if str1[end] not in dict_count:
            dict_count[(str1[end])] = 1
        else:
            dict_count[(str1[end])] += 1
        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(dict_count) > k:
            dict_count[str1[start]] -= 1
            if dict_count[str1[start]] == 0:
                del dict_count[str1[start]]
            start += 1 # shrink the window
        # remember the maximum length so far
        max_len = max(max_len, end - start + 1)
        end +=1
  return max_len


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2))) #4
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1))) #2
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3))) #5


main()