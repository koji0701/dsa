class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: 
            return max(nums)

        #skip last house 

        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, len(nums)-1): 
            cur = max(nums[i] + first, second) 
            first = second
            second = cur 
        
        firstRobAmt = max(first, second)

        #skip first house
        first = nums[1]
        second = max(nums[1], nums[2])
        
        for i in range(3, len(nums)): 
            cur = max(nums[i] + first, second) 
            first = second
            second = cur 
        
        return max(first, second, firstRobAmt)
