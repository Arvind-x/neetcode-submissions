class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        higher = [0]*len(prices)
        n = len(prices)
        higher[len(prices)-1] = prices[len(prices)-1]
        for i in range(n-2, -1, -1):
            higher[i] = max(prices[i], higher[i+1])

        for i in range(0, len(prices)):
            profit = max(profit, higher[i] - prices[i])
        
        return profit
        