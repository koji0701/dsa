class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #knapsack problem, two subsets equalling same means that 
        #can u find 1 subset where sum(nums)/2

        sumNum = sum(nums)
        if sumNum % 2 == 1: 
            return False 

        halfSum = sumNum // 2
        dp = [False] * (halfSum+1)
        dp[0] = True
        for num in nums: 
            for i in range(len(dp)-num-1, -1, -1):
                if dp[i]: 
                    dp[num+i] = True 

        print(dp)
        print('hi')
        return dp[-1]