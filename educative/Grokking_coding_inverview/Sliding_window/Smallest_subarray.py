'''
Given an array of positive numbers and a positive number ‘S,’
find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
'''
import math


def smallest_subarray_with_given_sum(s, arr):
  window_start = 0
  window_sum = 0
  window_end = 0
  min_len = math.inf
  while window_end < len(arr):
      window_sum += arr[window_end]  # add the next element
      # shrink the window as small as possible until the 'window_sum' is smaller than 's'
      while window_sum >= s:
          min_len = min(min_len, window_end - window_start + 1)
          window_sum -= arr[window_start]
          window_start += 1
      window_end += 1
  if min_len ==  math.inf:
      return 0
  return min_len


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))) #2
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))) #1
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))) #3


main()