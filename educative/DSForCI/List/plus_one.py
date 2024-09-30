#Time: O(n)
#Space: 1
'''Given: An array of non-negative digits that represent a decimal integer.
Problem: Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

we add 1 to the last element of the list A. Now we have to handle the carry as a result of this addition
Therefore, using a while loop, we iterate the list from the last index to the index 1
we check if we get 10 as a result of adding 1. If not, then the carry from the addition is 0, and we break the loop
However, if A[i] is 10 then we put 0 in its place and add 1 to the preceding index
This is repeated for every position in the list from the last index to index 1.
Now, we need to handle one other edge case, i.e., the value at the first index is 10. If A[0] is 10, we set A[0]
to 1 and append 0 to the list

'''
class Solution:
    def plus_one(self,A):
        i = len(A) - 1
        A[i] += 1
        while i > 0:
            if A[i] != 10:
                break
            A[i] = 0
            A[i - 1] += 1
            i -= 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)
        return A



if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.plus_one([1, 4, 9]) == [1, 5, 0])
    assert (s.plus_one([9, 9, 9]) == [1, 0, 0, 0])
