"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from collections import Counter


def compress_short(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    count = Counter(s)
    return "".join([k+str(v) for k,v in count.items()])

def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """
    if s == "":
        return s
    count = []
    c = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            c += 1
        else:
            count.append(s[i - 1] + str(c))
            c = 1
    count.append(s[-1] + str(c))

    return "".join(count)

from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        assert_equal(sol(''), '')
        assert_equal(sol('a'), 'a1')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)