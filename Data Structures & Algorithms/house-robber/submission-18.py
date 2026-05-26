class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return max(nums[0], nums[-1])
        first = nums[0]
        second = max(nums[0], nums[1])
        cur = 0

        for i in range(2, len(nums)): 
            cur = max(first + nums[i], second)
            first = second
            second = cur
        
        return max(first, second)