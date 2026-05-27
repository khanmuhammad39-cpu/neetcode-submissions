class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        sell_pointer = 1
        profit = 0

        while sell_pointer < len(prices):
            if prices[sell_pointer] > prices[buy_pointer]:
                profit += prices[sell_pointer] - prices[buy_pointer]

            buy_pointer += 1
            sell_pointer += 1

        return profit