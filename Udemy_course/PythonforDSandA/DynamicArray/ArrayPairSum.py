"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""


def pair_sum(arr, k):
    output = set()
    seen = set()
    for i,num in enumerate(arr):
        target = k - num
        if target in seen:
            output.add((min(target,num), max(target,num)))
        else:
            seen.add(num)
    return len(output)


class TestPair(object):

    def test(self, sol):
        assert sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10) == 6
        assert sol([1, 2, 3, 1], 3) == 1
        assert sol([1, 3, 2, 2], 4) == 2
        print
        'ALL TEST CASES PASSED'


# Run tests
t = TestPair()
t.test(pair_sum)