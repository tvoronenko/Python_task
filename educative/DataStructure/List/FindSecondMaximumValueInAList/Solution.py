#complexity time O()
#space complexity O()

class Solution:
    def find_second_maximum(self, lst):
        if len(lst) == 1:
            return lst[0]
        if len(lst) == 2:
            return min(lst)
        max_1 = max(lst[0], lst[1])
        max_2 = min(lst[0], lst[1])
        for i in range(1, len(lst)):
            if lst[i] >= max_1:
                max_2 = max_1
                max_1 = lst[i]
            elif (lst[i] > max_2):
                max_2 = lst[i]

        return max_2


if __name__ == '__main__':
    # begin
    s = Solution()
    assert s.find_second_maximum([9,2,3,6]) == 6
    assert s.find_second_maximum([4, 2, 1, 5, 0]) == 4