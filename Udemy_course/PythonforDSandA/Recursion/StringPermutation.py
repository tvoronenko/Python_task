"""
RUN THIS CELL TO TEST YOUR SOLUTION.
"""

from nose.tools import assert_equal
def permute(s):
    if len(s) == 1:
        return [s]
    output = []
    for i in range(len(s)):
        list_p = permute(s[:i]+s[i+1:])
        for perm in list_p:
            output += [s[i] + perm]
    return output

class TestPerm(object):

    def test(self, solution):
        assert_equal(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print
        'All test cases passed.'


# Run Tests
t = TestPerm()
t.test(permute)