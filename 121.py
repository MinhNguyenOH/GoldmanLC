class Solution(object):
    def maxProfit(self, prices) -> int:
        maxprofit = 0
        minprice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - minprice)
        return maxprofit
