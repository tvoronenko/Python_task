#complexity time O()
#space complexity O()
from typing import List

class Solution:
    def right_rotate(self,lst, k):
        if lst == []:
            return []
        k = k % len(lst)
        for i in range(k):
            num = lst[-1]
            del lst[-1]
            lst.insert(0, num)
        return lst

    def right_rotate1(lst, k):
        if len(lst) == 0:
            k = 0
        else:
            k = k % len(lst)
        rotatedList = []
        # get the elements from the end
        for item in range(len(lst) - k, len(lst)):
            rotatedList.append(lst[item])
        # get the remaining elements
        for item in range(0, len(lst) - k):
            rotatedList.append(lst[item])
        return rotatedList

if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.right_rotate([10,20,30,40,50],3) == [30,40,50,10,20]