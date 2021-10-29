class Solution:
    def maxProfit(self, prices):
        # maximum profit
        max_profit = 0
        # current max_prices
        max_prices = prices[-1]
        # go thru all prices from end
        for i in range(len(prices)-2,0,-1):
            # change max_price if current price is bigger
            if prices[i] > max_prices:
                max_prices = prices[i]
            # if current price is smaller than max_price, calc profit ans select max_profit
            else:
                max_profit = max(max_profit, max_prices - prices[i])
        return max_profit



if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) #5
    print(s.maxProfit([7,6,4,3,1])) # 0
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0