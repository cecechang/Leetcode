class Solution(object):
    def maxProfit(self, prices):
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = max((prices[r]-prices[l]), profit)
            else:
                l=r
            r+=1
        return profit

