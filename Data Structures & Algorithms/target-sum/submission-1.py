class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #knapsack, where u can +/- every num 
        #combinations, not permutations. for num is the outside 

        dp = defaultdict(int) #unlimited range here since neg nums 
        dp[0] = 1 #base case 
        for num in nums: 
            newDic = defaultdict(int)
            for key, val in dp.items(): 
                newDic[key - num] += val 
                newDic[key + num] += val
            
            dp = newDic
        
        return dp[target]

        