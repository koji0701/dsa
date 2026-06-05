class Solution:
    #modified kadanes algorithm, just use products 
    #and also keep track of the min product (negative val), since this 
    #can easily become the max 
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0]
        globalMax = nums[0]
        for i in range(1, len(nums)): 
            num = nums[i]
            prevMax = maxProduct #careful not to double multiply
            maxProduct = max(num, maxProduct*num, minProduct*num)
            minProduct = min(num, prevMax*num, minProduct*num)

            globalMax = max(globalMax, maxProduct) 
            #print(num, maxProduct, minProduct, globalMax)
        
        return globalMax
