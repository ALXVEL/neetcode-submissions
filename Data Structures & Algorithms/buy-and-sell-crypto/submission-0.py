class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_profit = 0
        
        buy = 0
        for sell in range(1, len(prices)):
            curr_profit = prices[sell] - prices[buy]
            
            if prices[sell] < prices[buy]:
                buy = sell
            
            max_profit = max(curr_profit, max_profit)
        
        return max_profit