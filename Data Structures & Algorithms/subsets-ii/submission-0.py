class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        rv = []
        nums.sort() 

        def backtrack(start: int, cur: List[int]): 
            rv.append(cur[:])
            if len(cur) == len(nums): 
                return
            for i in range(start, len(nums)): 
                num = nums[i]
                if i > start and num == nums[i-1]:
                    continue
                cur.append(num)
                backtrack(i+1, cur) 
                cur.pop(-1) 
            
        backtrack(0, [])
        return rv