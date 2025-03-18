"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
def finder(arr1, arr2):
    missing = 0
    for num in arr1:
        missing = missing ^ num
        
    for num in arr2:
        missing = missing ^ num

    return missing



class TestFinder(object):

    def test(self, sol):
        assert sol([5, 5, 7, 7], [5, 7, 7])==5
        assert sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])== 5
        assert sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])== 6
        print
        'ALL TEST CASES PASSED'


# Run test_show.py
t = TestFinder()
t.test(finder)