class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rv = []
        def isPalindrome(start: int, end: int) -> bool:
            while start < end: 
                if s[start] == s[end]: 
                    start += 1 
                    end -= 1
            
                else: 
                    return False 
            return True

        def backtrack(idx, cur): 
            nonlocal rv
            if idx >= len(s): 
                rv.append(cur[:])
                return
            for i in range(idx, len(s)): 
                if isPalindrome(idx, i): 
                    cur.append(s[idx:i+1])
                    backtrack(i+1, cur)
                    cur.pop()
        
        backtrack(0, [])
        return rv
