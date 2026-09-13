#bfs sol, then ill do union find 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = ((1,0), (0,1), (-1,0), (0,-1))
        #seen = 2
        def bfs(fr: int, fc: int): 
            q = deque()
            size = 1
            q.append((fr,fc))
            while q: 
                r, c = q.popleft() 

                for dr, dc in dirs: 
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]): 
                        if grid[nr][nc] != 1: 
                            continue 
                        size += 1
                        q.append((nr, nc))
                        grid[nr][nc] = 2
        
            return size 
        maxSize = 0
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if (grid[i][j] == 1): 
                    grid[i][j] = 2
                    maxSize = max(maxSize, bfs(i,j))
        
        return maxSize




