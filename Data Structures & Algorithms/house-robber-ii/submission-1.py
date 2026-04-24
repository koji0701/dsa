'''
same as regular house robber, where u do dp with recurrence 
since its a circle, u can either have the first house or last house 
thus, we can just do two house robbers. one including first house, one including 
last house 


'''

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3: 
            return max(nums)
        #memo's for houses 
        first = [0]*len(nums)
        last = [0]*len(nums)

        first[0] = nums[0]
        first[1] = max(nums[0], nums[1])

        last[1] = nums[1]

        for i in range(2, len(nums)): 
            last[i] = max(last[i-2] + nums[i], last[i-1])

            if i < len(nums) - 1: 
                first[i] = max(first[i-2]+ nums[i], first[i-1])


        return max(first[-2], last[-1])











