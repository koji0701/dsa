class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        rv = [0] * (len(nums) - (k-1))

        maxIdx = -1 
        curMax = -99999999

        for i in range(len(nums) - (k-1)): 
            j = i+(k-1)

            if i > maxIdx: 
                curMax = -999999999

                for nmi in range(i, j+1): 
                    if nums[nmi] >= curMax: 
                        curMax = nums[nmi]
                        maxIdx = nmi 

            else: 
                if nums[j] >= curMax: 
                    curMax = nums[j]
                    maxIdx = j

            rv[i] = curMax 

        return rv
            
