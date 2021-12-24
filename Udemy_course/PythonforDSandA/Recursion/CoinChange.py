"""
RUN THIS CELL TO TEST YOUR FUNCTION.
NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION
"""
import math

from nose.tools import assert_equal
def rec_coin_rec(target,coins):
    if target == 0:
        return 0
    f = math.inf
    for coin in coins:
        if (target - coin) >=0:
            f = min(f,1+rec_coin_rec((target - coin),coins) )
    return f

def rec_coin(target,coins):
    dp = [target] * (target +1)
    dp[0] = 0
    for cent in range(1, target+1):
        for coin in coins:
            if (cent - coin) >= 0:
                dp[cent] = min(dp[cent],1+dp[cent - coin])
    return dp[-1]

class TestCoins(object):

    def check(self, solution):
        coins = [1, 5, 10, 25]
        assert_equal(solution(10, coins), 1)
        assert_equal(solution(45, coins), 3)
        assert_equal(solution(23, coins), 5)
        assert_equal(solution(74, coins), 8)

        print
        'Passed all tests.'


# Run Test

test = TestCoins()
test.check(rec_coin)