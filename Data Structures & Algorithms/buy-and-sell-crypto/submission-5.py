class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1 # buy is left, sell is right
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l] # buy low sell high
            if profit < 0:
                l = r
            else:
                max_profit = max(max_profit,profit)
            r += 1
        
        return max_profit
        