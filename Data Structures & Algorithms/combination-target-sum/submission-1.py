class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        rv = []
        nums.sort() 

        def backtrack(start: int, combo: List[int]): 
            curSum = sum(combo)
            if curSum == target: 
                rv.append(combo[:])
                return 
            for i in range(start, len(nums)): 
                if curSum + nums[i] > target: 
                    break
                combo.append(nums[i])
                backtrack(i, combo)
                combo.pop(-1) 
        
        backtrack(0, [])
        return rv