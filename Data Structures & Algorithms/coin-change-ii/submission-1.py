class Solution:
    #knapsack, can use unlimited
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1) #idx is sum, val is amt of ways 
        dp[0] = 1
        for coin in coins: 
            for i in range(len(dp)-coin): 
                if dp[i] != 0: 
                    dp[i+coin] += dp[i]
        return dp[-1]




