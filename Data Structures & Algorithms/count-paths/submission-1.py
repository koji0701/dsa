'''
dp: amt of ways to get to every cell is just 
sum of every way for cell above it and left of it 

initialize top row and left column to be 1
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numPaths = [[0 for _ in range(n)] for _ in range(m)]

        numPaths[0] = [1] * n
        for row in range(m): 
            numPaths[row][0] = 1
        
        for row in range(1, m): 
            for col in range(1, n): 
                numPaths[row][col] = numPaths[row-1][col] + numPaths[row][col-1]
        
        return numPaths[-1][-1]