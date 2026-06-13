

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rv = []

        def backtrack(cur: str, numOpen: int): 
            if len(cur) == 2*n:
                nonlocal rv
                rv.append(cur[:])
                return 
            
            numClosed = len(cur) - numOpen 
            if numOpen >= numClosed: 
                #open or closed okay
                if numOpen < n: 
                    #can do open 
                    backtrack(cur+"(", numOpen +1)
                
                if numOpen > numClosed: 
                    backtrack(cur+")", numOpen) 
            
        
        backtrack("", 0)
        return rv
            
            






            