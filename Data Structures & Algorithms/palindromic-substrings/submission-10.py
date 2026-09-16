class Solution:
    def countSubstrings(self, s: str) -> int:
        #construct a 2d grid
        grid = [[False for _ in range(len(s))] for _ in range(len(s))]

        #true means palindromic 
        #main diagonal is single char length 
        palis = 0


        #build from bottom up, so smaller string to larger
        #if the outer two chars are the same, and 
        #the inner portion is a palindrome, then pali 

        #inner portion is a palindrome when 
        #grid[st+1][en-1] is true
        for st in range(len(s)-1, -1, -1): 
            for en in range(st, len(s)): 
                

                if s[st] == s[en] and (en - st < 2 or grid[st + 1][en - 1]):

                    grid[st][en] = True
                    palis += 1

        
        return palis 


