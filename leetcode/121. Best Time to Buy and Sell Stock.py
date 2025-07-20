#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 # l = buy
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[l] < prices[i]:
                profit = prices[i] - prices[l]
                max_profit = max(profit,max_profit)
            else:
                l = i
        
        return max_profit
