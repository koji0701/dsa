'''
intuition: 
- grid: word1 x word2
    - first row and first col are empty string and initialized to 0 for ez base cases
    - word1 is col, word2 is row
- if letters are same at that cell, 0 extra operations
    - cell = diagonally left above it
- if letters are diff at that cell, 1 extra operation
    - cell = min(cell above, cell left) + 1
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        operations = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

        #first row and col are empty string, so initialize these with values 

        operations[0] = [i for i in range(len(word1)+1)]
        for i in range(len(word2)+1):
            operations[i][0] = i

        for row in range(1, len(operations)): 
            for col in range(1, len(operations[0])): 
                if word1[col-1] == word2[row-1]: 
                    operations[row][col] = operations[row-1][col-1]
                else: 
                    operations[row][col] = min(operations[row-1][col], operations[row][col-1], operations[row-1][col-1]) + 1
        print(operations)
        return operations[-1][-1]






