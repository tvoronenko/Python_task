#Time: O(n)
#Space: 1
'''
Given: Given two sorted arrays, A and B, determine their intersection. What elements are common to A and B?
i and j have been set to 0.
result_list has been initialized to an empty list.
The while loop is where the crux of the algorithm lies. The while loop will terminate as soon as i or j becomes equal
or greater than the length of the arrays they are iterating on.
One of these conditions is when we check for duplicates using the condition (A[i] != A[i - 1])
In that case, we need to handle the code when i equals 0. Therefore, we have an additional check, i.e., i == 0.
Therefore, if i equals 0, there is no need to check for the duplicate condition (A[i] != A[i - 1]) .
Instead, A[i] is appended to result_list if A[i] equals B[j] and i equals 0.

After the while loop terminates, result_list is returned from the function.
'''

class Solution:
    def intersect_sorted_array(self,A, B):
        i,j = 0,0
        result_list = []
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                if i == 0 or A[i] != A[i-1]:
                    result_list.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1

        return result_list


if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.intersect_sorted_array([2, 3, 3, 5, 7, 11], [3, 3, 7, 15, 31]) == [3, 7])

