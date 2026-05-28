from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s) 
        rv = 0

        @lru_cache(maxsize=None)
        def isPalindrome(start: int, end: int) -> bool:
            if start >= end: 
                return True 
            
            if s[start] == s[end]: 
                return isPalindrome(start+1, end-1)
            
            return False


        for i in range(n):
            for j in range(i, n): 
                if isPalindrome(i, j): 
                    rv += 1
        
        return rv