class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rv = []
        def backtrack(start: int, subset: List[int]): 
            rv.append(subset[:])
            for i in range(start, len(nums)): 
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop(-1)
        
        backtrack(0, [])
        return rv