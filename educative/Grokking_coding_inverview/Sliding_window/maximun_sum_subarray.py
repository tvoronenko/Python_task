'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
Time complexity O(n)
Space complexity O(1)
'''

def max_sub_array_of_size_k(k, arr):
  window_start = 0
  window_end = 0
  sum_max = 0
  window_sum = 0
  while window_end < len(arr):
      window_sum += arr[window_end]  # add the next element
      # slide the window, we don't need to slide if we've not hit the required window size of 'k'
      window_end += 1
      if window_end >= k:
          sum_max = max(sum_max, window_sum)
          window_sum -= arr[window_start]  # subtract the element going out
          window_start += 1  # slide the window ahead

  return sum_max

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))) #9
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))) #7


main()