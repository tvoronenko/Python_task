"""
RUN THIS CELL TO TEST YOUR CODE>
"""


from nose.tools import assert_equal
def uni_char(s):
    count = set()
    for ch in s:
        if ch in count:
            return False
        else:
            count.add(ch)
    return True

class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print( 'ALL TEST CASES PASSED')


# Run Tests
t = TestUnique()
t.test(uni_char)