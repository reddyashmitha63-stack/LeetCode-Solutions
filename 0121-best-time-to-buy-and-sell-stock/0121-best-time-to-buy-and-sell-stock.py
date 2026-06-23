class Solution(object):
    def maxProfit(self, prices):
        size=len(prices)
        mini=prices[0]
        profit=0
        for i in range(1,size):
            cost=prices[i]-mini
            profit=max(profit,cost)
            mini=min(mini,prices[i])
        return profit
        