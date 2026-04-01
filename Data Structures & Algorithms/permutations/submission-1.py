class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #permutations means only return the leaves 
        rv = []
        #sort to deduplicate naturally
        nums.sort() 

        def backtrack(start: int, sub: List[int]): 
            #check if leaf 
            if start == len(nums):  
                rv.append(sub[:])
                return 
            
            #permutations, swap two elems i and start
            for i in range(start, len(nums)): 
                sub[start], sub[i] = sub[i], sub[start]
                backtrack(start+1, sub) 
                #start+1 since backtracking, 
                #and wanting to traverse layers 
                #after traversing layers, eventually get to leaves
                sub[start], sub[i] = sub[i], sub[start]
                
        backtrack(0, nums)
        return rv