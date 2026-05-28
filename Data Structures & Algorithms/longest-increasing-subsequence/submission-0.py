class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums): 
            j = 0 
            while j < i: 
                if num > nums[j]: 
                    subseq[i] = max(subseq[i], subseq[j]+1) 
                j+=1
                
        return max(subseq)






