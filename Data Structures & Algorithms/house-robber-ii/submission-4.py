class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: 
            if len(nums) <= 2: 
                return max(nums[0], nums[-1])
            return max(nums[0], nums[-1], nums[-2])

        firstRobAmt = [0] * (len(nums)-1) #discluding last house 
        lastRobAmt = [0] * (len(nums)-1) #discluding first house, iterate backwards 

        #first house 
        firstRobAmt[0] = nums[0]
        firstRobAmt[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)-1): 
            firstRobAmt[i] = max(firstRobAmt[i-2] + nums[i], firstRobAmt[i-1])
        
        lastRobAmt[-1] = nums[-1]
        lastRobAmt[-2] = max(nums[-1], nums[-2])
        print(len(lastRobAmt))
        print(lastRobAmt)

        for i in range(len(lastRobAmt)-3, -1, -1): 
            print(i)
            lastRobAmt[i] = max(lastRobAmt[i+2] + nums[i+1], lastRobAmt[i+1])
        print(lastRobAmt)
        return max(firstRobAmt[-1], firstRobAmt[-2], lastRobAmt[0], lastRobAmt[1])

