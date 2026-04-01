class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 

        rv = set()
        def backtrack(start: int, combo: List[int]): 
            su = sum(combo)
            for i in range(start, len(candidates)): 
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                num = candidates[i]
                if su + num == target:                     
                    newC = tuple(combo) + (num,)
                    rv.add(newC)
                    continue
                if su + num > target: 
                    break #since sorted
                combo.append(num) 
                backtrack(i+1, combo) 
                combo.pop(-1) 
        backtrack(0,[])
        rv = [list(t) for t in rv]

        return list(rv) 