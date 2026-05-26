class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = set()
        cubes = [[set() for _ in range(3)] for _ in range(3)]
        cols = [set() for _ in range(9)] 
        
        for row in range(len(board)): 
            seenRow = set()
            for col in range(len(board[0])): 
                cur = board[row][col]
                if cur == ".": 
                    continue 
                if cur in seenRow or cur in cubes[row // 3][col // 3] or cur in cols[col]:
                    return False 
                seenRow.add(cur) 
                cubes[row // 3][col // 3].add(cur) 
                cols[col].add(cur) 
        
        return True