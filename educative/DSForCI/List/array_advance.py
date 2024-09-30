#Time: O(n)
#Space: 1
'''
Problem: Is it possible to advance from the start of the array to the last element given that the maximum you can
advance from a position is based on the value of the array at the index you are currently present on?
 
i > max_furute_index: This implies that the end is not reachable.
max_furute_index >= last_idx : This implies that the end is reachable.

In each iteration of the while loop, we update max_furute_index to the maximum of max_furute_index and (A[i] + i) . 
i increments by 1 in the next line.

After the while loop terminates, we’ll check for the condition which terminates the while loop. 
If max_furute_index >= last_idx, then True is returned from the function. Otherwise, False is returned.
'''

class Solution:
    def array_advance(self,A):
        max_future_idx = 0
        last_idx = len(A) - 1
        i = 0
        while i<= max_future_idx <= last_idx:
            max_future_idx = max(max_future_idx, A[i] + i)
            i += 1

        return max_future_idx >= last_idx




if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.array_advance([3, 3, 1, 0, 2, 0, 1]) == True)
    assert (s.array_advance([3, 2, 0, 0, 2, 0, 1]) == False)
    assert (s.array_advance([2, 4, 1, 1, 0, 2, 3]) == True)
