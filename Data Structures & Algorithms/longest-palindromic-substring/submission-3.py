'''
interval dp
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1 : 
            return s
        n = len(s)
        palSub = [[False for _ in range(n)] for _ in range(n)]

        #diagonal is palindrome, since a single letter is palindrome
        for i in range(n): 
            palSub[i][i] = True
        
        #iterate over intervals 
        longest = 1
        rv = s[0]
        for interval in range(1, n): 
            row = 0 
            startCol = row + interval
            for col in range(startCol, n):
                #if 2 outer letters the same, its a palindrome if the inside is palindrome 
                #inside is a palindrome if the smaller interval inside is a palindrome
                if s[row] == s[col]: 
                    #edge case for interval=1
                    val = palSub[row+1][col-1] if row+1 <= col-1 else True
                    palSub[row][col] = val
                    if palSub[row][col] and interval + 1 > longest: 
                        longest = interval + 1 
                        rv = s[row:col+1]
                else: 
                    palSub[row][col] = False
                
                row += 1

        print(longest)
        return rv




