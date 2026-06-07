class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #index: day 
        #value: max profit at that day.
        #prices[i] - minPriceSeen
        #dp = [0] * len(prices) 
        minPriceSeen = prices[0]

        #space optimize: no need for dp array, just track the max profit
        #max(maxProfit, prices[i] - minPriceSeen)
        maxProfit = -9999

        for i in range(len(prices)): 
            maxProfit = max(maxProfit, prices[i] - minPriceSeen)
            minPriceSeen = min(minPriceSeen, prices[i])

        return maxProfit

