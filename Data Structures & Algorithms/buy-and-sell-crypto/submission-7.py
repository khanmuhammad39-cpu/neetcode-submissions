class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #buy pointer (should be min)
        right = 1 # sell pointer(should be max)
        best_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > best_profit:
                    best_profit = profit
            else:
                left = right
            
            right += 1
        
        return best_profit
        