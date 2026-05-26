'''
dp: amt of ways to get to every cell is just 
sum of every way for cell above it and left of it 

initialize top row and left column to be 1
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        newRow = [0] * n 
        newRow[0] = 1

        print(row)

        for r in range(1,m): 
            for col in range(1,n): 
                newRow[col] = newRow[col-1] + row[col]
            
            row = newRow
        
        return row[-1]





