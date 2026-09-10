class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxima = 0
        for buy in range(len(prices)):
            for sell in range(buy, len(prices)):
                profit = prices[sell] - prices[buy]
                maxima = max(maxima, profit)
        return maxima