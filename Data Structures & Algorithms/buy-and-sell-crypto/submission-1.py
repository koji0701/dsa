class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #index: day 
        #value: max profit at that day.
        #prices[i] - minPriceSeen
        dp = [0] * len(prices) 
        minPriceSeen = prices[0]

        for i in range(len(prices)): 
            dp[i] = prices[i] - minPriceSeen
            minPriceSeen = min(minPriceSeen, prices[i])

        return max(dp)

