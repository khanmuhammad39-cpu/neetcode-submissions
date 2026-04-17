class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best_profit = 0
        # [10,1,5,6,7,1]
        # profit = sell - buy
        # sell should be highest
        # buy should be lowest
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                if profit > best_profit:
                    best_profit = profit
        
        return best_profit
        