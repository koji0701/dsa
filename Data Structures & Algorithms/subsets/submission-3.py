class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rv = []
        
        def backtrack(idx, cur): 
            nonlocal rv 
            rv.append(cur[:])
            for i in range(idx, len(nums)): 
                cur.append(nums[i])
                backtrack(i+1, cur) 
                cur.pop()
        
        backtrack(0,[])
        return rv

            
