#just queen cant be in same row or col or diag
#keep track of col set 
#diag: if (row+col) or (row+col-n) r same, 
    #keep track of pos and neg in sets too 
#iterate through rows to keep unique

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n 
        #there are (2*n-1) total diags, but lets 1-index it to keep it simple
        posDiag = [False] * (2*n) #row+col
        negDiag = [False] * (2*n) #abs(row-col)
        rv = []

        
        board = [["." for _ in range(n)] for _ in range(n) ]

        def backtrack(row: int): 
            if row == n: 
                #join every column 
                joined = ["".join(board[i]) for i in range(len(board))]
                rv.append(joined)
                return
            
            for col in range(n): 
                if cols[col]: 
                    continue
                if posDiag[row+col] or negDiag[(row-col)+n]: 
                    continue 
                
                cols[col] = True 
                posDiag[row+col] = True 
                negDiag[(row-col)+n] = True
                board[row][col] = "Q"
                backtrack(row+1) 
                cols[col] = False 
                posDiag[row+col] = False 
                negDiag[(row-col)+n] = False
                board[row][col] = "."
        
        backtrack(0) 
        return rv
                








