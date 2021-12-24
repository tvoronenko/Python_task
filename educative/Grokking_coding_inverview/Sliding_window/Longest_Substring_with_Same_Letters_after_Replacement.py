'''
Given a string with lowercase letters only, if you are allowed to replace no more than
k letters with any letter, find the length of the longest substring having the same
letters after replacement.
Time: O(N)
Space: O(1)
'''
from collections import defaultdict


def length_of_longest_substring(str, k):
  start = 0
  end = 0
  max_len = 0
  dict_count = defaultdict(int)
  max_repeat_letter_count = 0
  while end < len(str):
      dict_count[str[end]] +=1
      max_repeat_letter_count = max(max_repeat_letter_count, dict_count[str[end]])
      # Current window size is from window_start to window_end, overall we have a letter which is
      # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
      # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
      # if the remaining letters are more than 'k', it is the time to shrink the window as we
      # are not allowed to replace more than 'k' letters
      if (end - start + 1 - max_repeat_letter_count) > k:
          dict_count[str[start]] -= 1
          start += 1
      max_len = max(max_len, end - start + 1)
      end += 1
  return max_len


def main():
  print(length_of_longest_substring("aabccbb", 2)) #5
  print(length_of_longest_substring("abbcb", 1)) #4
  print(length_of_longest_substring("abccde", 1)) #3


main()