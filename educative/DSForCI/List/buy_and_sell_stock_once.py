# Time Complexity: O(n)
# Space Complexity: O(1)
'''Given: Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be
made from buying on one day and selling on another.
In an array of prices, each index represents a day, and the value on that index represents the price of the stocks on that day.
Here is the way to calculate the profit:
Profit = Selling Price - Buying Price
Note that you need to buy the stocks before you sell them so the day (index) indicating the buying price should be
before the day (index) indicating the selling price.

We set max_profit and min_price to 0 and infinity respectively. The list prices is iterated using a for loop
As we are supposed to keep track of the minimum price, we update min_price using the min function where min_price is
the minimum amount between min_price and price of the current iteration. In the next line, we store the calculated
profit (price - min_price) in compare_profit. As we also need to keep a check on the max_profit, we update max_profit
to the maximum value between max_profit and compare_profit. After we are done with the iteration of prices,
 we return max_profit on.
'''

class Solution:
    def buy_and_sell_stock_once(self,prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit




if __name__ == '__main__':
    # begin
    s = Solution()
    assert (s.buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30)
    assert (s.buy_and_sell_stock_once([100, 180, 260, 310, 40, 535, 695])== 655)
    assert (s.buy_and_sell_stock_once([50, 40, 30, 20, 10]) == 0)
    assert (s.buy_and_sell_stock_once([110, 215, 180, 335, 5]) == 225)
