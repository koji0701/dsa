class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * len(cost) 
        minCost[0] = cost[0]
        minCost[1] = cost[1]

        for i in range(2, len(cost)): 
            minCost[i] = min(minCost[i-1], minCost[i-2]) + cost[i]
        
        return min(minCost[-2], minCost[-1])