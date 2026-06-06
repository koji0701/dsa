class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: 
            return []
        mp = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

        rv = []
        
        def backtrack(cur: List[str]):
            if len(cur) >= len(digits): 
                nonlocal rv
                rv.append("".join(cur))
                return  
            
            digi = digits[len(cur)]
            for l in mp[digi]: 
                cur.append(l) 
                backtrack(cur)
                cur.pop()
        
        backtrack([])
        return rv




