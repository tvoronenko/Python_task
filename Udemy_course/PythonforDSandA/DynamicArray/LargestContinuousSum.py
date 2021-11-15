import math


def large_cont_sum(arr):
    sum_sub = arr[0]
    curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        sum_sub = max(sum_sub,curr_sum)
    return sum_sub


class LargeContTest(object):
    def test(self, sol):
        assert sol([1, 2, -1, 3, 4, -1]) == 9
        assert sol([1, 2, -1, 3, 4, 10, 10, -10, -1]) == 29
        assert sol([-1, 1]) == 1
        print
        'ALL TEST CASES PASSED'


# Run Test
t = LargeContTest()
t.test(large_cont_sum)