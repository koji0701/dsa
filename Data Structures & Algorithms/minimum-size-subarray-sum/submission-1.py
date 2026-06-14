class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:            
        prefixSum = 0
        i = 0 
        j = 0
        minLen = 9999999
        while i<len(nums): 
            print(i, j, prefixSum)
            if prefixSum < target: 
                if j >= len(nums): 
                    break
                prefixSum += nums[j]
                j += 1
                continue 
            
            #dec from left 
            minLen = min(j - i , minLen)
            prefixSum -= nums[i]
            i += 1
        
        if minLen == 9999999: return 0

        return minLen