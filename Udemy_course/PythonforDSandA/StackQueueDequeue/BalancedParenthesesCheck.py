"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

def balance_check(s):
    dict = {"}": "{", ")": "(", "]": "["}
    if s == "":
        return True

    stack = [s[0]]
    for i in range(1,len(s)):
        if s[i] in dict:
            open = stack.pop()
            if dict[s[i]] != open:
                return False
        else:
            stack.append(s[i])
    if len(stack) != 0 :
        return False
    return True

class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)