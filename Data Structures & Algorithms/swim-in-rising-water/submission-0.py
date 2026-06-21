'''
t = highest num on the path from top left to bottom right 
    - must be >= bottom right num

explore the paths with the lowest maxNum first 
- priority queue, where first num of tuple is the maxNum 
- (maxNum, r, c)
- backtracking dfs approach where u 
"-1" out the grid for seen cells. u need a global visited set anyway, 
since at every point u couldve made a decision to go onto that path

Runtime: O(n^2 log n). Traverse n^2 cells and log n additions for pq 
Space: O(n^2) at very worse. max num of elements in the pq. 
in most cases will be way less tho 

'''

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [] #(maxNum, r, c)
        heapq.heapify(pq) 
        heapq.heappush(pq, (grid[0][0], 0, 0))

        n = len(grid)
        directions = ((1,0), (0,1), (-1,0), (0,-1)) #inorder of bias 

        while pq: 
            curMax, r, c = heapq.heappop(pq) 
            if grid[r][c] == -1: 
                continue 
            if r == n-1 and c == n-1: 
                return curMax
            grid[r][c] = -1
            for dr, dc in directions: 
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n: 
                    if grid[nr][nc] != -1: 
                        newMax = max(grid[nr][nc], curMax)
                        heapq.heappush(pq, (newMax, nr, nc))
        

        





        







