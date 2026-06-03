class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [99999999] * (amount+1)
        dp[0] = 0

        for coin in coins: 
            for i in range(coin, amount+1): 
                dp[i] = min(dp[i-coin] + 1, dp[i])
        
        if dp[-1] == 99999999: 
            return -1 
        return dp[-1]