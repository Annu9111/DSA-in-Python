#question:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #bruitfull solution
        n=len(prices)
        max_profit=0
        for i in range(n):
            p=prices[j]-prices[i]
            max_profit=max(max_profit,p)
        return max_profit
    
        #optimal solution
        max_profit=0
        max_price=float("-inf")
        n=len(prices)
        for i in range(0,n):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit    
        
        