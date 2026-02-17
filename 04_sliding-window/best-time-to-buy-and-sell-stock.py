"""
Makes sense; look at code. If current price is lower than buy, overwrite buy.
Check if current profit overwrite's overall maxProfit. Return maxProfit
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price
            max_profit = max(max_profit, price - buy)

        return max_profit
