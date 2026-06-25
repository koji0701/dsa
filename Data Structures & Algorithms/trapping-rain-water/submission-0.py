class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n 

        for i in range(0, n-1): 
            maxLeft[i+1] = max(maxLeft[i], height[i])

        for i in range(len(height)-1, 0, -1): 
            maxRight[i-1] = max(maxRight[i], height[i])
        
        area = 0 
        for i in range(n): 
            capture = min(maxLeft[i], maxRight[i]) - height[i]
            area += max(0, capture)
        return area