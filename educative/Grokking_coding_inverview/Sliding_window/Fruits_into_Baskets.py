'''
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
Time: O(N)
Space: O(1)

'''
import math


def fruits_into_baskets(fruits):
    start = 0
    end = 0
    max_len = 0
    dict_count = {}
    # try to extend the range [window_start, window_end]
    while end < len(fruits):
        if fruits[end] not in dict_count:
          dict_count[fruits[end]] = 1
        else:
          dict_count[fruits[end]] += 1
        # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
        while len(dict_count) > 2:
            dict_count[fruits[start]] -= 1
            if dict_count[fruits[start]] == 0:
                del dict_count[fruits[start]]
            start += 1# shrink the window
        max_len = max(max_len, end - start + 1)
        end += 1
    return max_len



def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))) #3
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))) #5


main()
