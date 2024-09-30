#Time: O(n)
#Space: 1
#for set
#Time: O(n)
#Space: O(n)
'''
Given: Given an array of integers, return True or False if the array has two numbers that add up to a specific target.
 You may assume that each input would have exactly one solution.
Approach 1 with set:
we use a set and using a for loop, we iterate over A calculate target - A[i] and check if it is present in set or not.
If it’s not, we store A[i]. Now it is easy for us to check for the next elements if we ever come across an element
which is equal to target - A[i].
If A[i] in any iteration is present in set, we found out pair.

Approach 2:
This approach assumes that the array is sorted. So i and j are set to 0 and len(A) - 1 respectively ,
i.e., the minimum and the maximum value. A while loop is set which will run as long as i < j.
If at any iteration, A[i] + A[j] equal target, we have found the pairs and we return True from the function after
printing the pairs. However, if the sum of A[i] and A[j] is less than target, we increment i by 1,
so that A[i] will be a greater value in the next iteration and will produce a greater sum than the current sum.
On the other hand, if the sum of A[i] and A[j] is greater than target, we decrement j to achieve a lesser sum by moving
to an index with a smaller value. After the while loop terminates, we return False as we never come across a pair which
sums to target during the execution of the while loop.
'''


class Solution:
    def two_sum_set(self,A, target):
        set_numbers = set()
        for i in range(len(A)):
            if (target - A[i]) in set_numbers:
                print(A[i], target - A[i])
                return True
            else:
                set_numbers.add(A[i])

        return False

    #only if array is sorted
    def two_sum(self, A, target):
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] == target:
                print(A[i], A[j] )
                return True
            elif A[i] + A[j] < target:
                i += 1
            else:
                j -= 1
        return False

        

if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.two_sum_set([-2, 1, 2, 4, 7, 11],13) == True)
    assert (s.two_sum([-2, 1, 2, 4, 7, 11], 13) == True)

