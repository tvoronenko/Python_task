'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
find the length of the longest contiguous subarray having all 1s.

'''
from collections import defaultdict


def length_of_longest_substring1(arr, k):
    start = 0
    end = 0
    max_len = 0
    max_ones_count = 0
    while end < len(arr):
        if arr[end] == 1:
            max_ones_count += 1
        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (end - start + 1 - max_ones_count) > k:
            if arr[start] == 1:
                max_ones_count -= 1
            start += 1

        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len

def length_of_longest_substring(str, k):
  start = 0
  end = 0
  max_len = 0
  dict_count = defaultdict(int)
  max_repeat_letter_count = 0
  while end < len(str):
      dict_count[str[end]] +=1
      if str[end] == 1:
        max_repeat_letter_count = max(max_repeat_letter_count, dict_count[str[end]])
      # Current window size is from window_start to window_end, overall we have a letter which is
      # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
      # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
      # if the remaining letters are more than 'k', it is the time to shrink the window as we
      # are not allowed to replace more than 'k' letters
      if (end - start + 1 - max_repeat_letter_count) > k:
          if str[start] == 1:
              max_repeat_letter_count = max(max_repeat_letter_count, dict_count[str[start]])
          dict_count[str[start]] -= 1
          start += 1
      max_len = max(max_len, end - start + 1)
      end += 1
  return max_len





def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)) #6
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)) #9


main()