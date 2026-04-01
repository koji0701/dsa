'''
approach: 
- iterative bfs, beginning at the edges
- from the edges, have the algorithm go uphill instead of downhill
- any neighboring cell where i can go uphill to is seen in that ocean
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = (
            (1,0), 
            (0,1), 
            (-1,0), 
            (0,-1)
        )
        
        def bfs(initialEdges: List[Tuple[int,int]]) -> Set[Tuple[int, int]]: 
            queue = deque(initialEdges) 
            ocean = set() 
            ocean.update(initialEdges) 

            while queue: 
                r,c = queue.popleft()
                for dr, dc in directions: 
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr,nc) not in ocean:
                    
                        ocean.add((nr,nc))
                        queue.append((nr,nc))
        
            return ocean
        
        rows = len(heights)
        cols = len(heights[0])
        initialPacific = [(r, 0) for r in range(len(heights))] + [(0, c) for c in range(len(heights[0]))]
        initialAtlantic = [(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)]

        pacific = bfs(initialPacific) 
        atlantic = bfs(initialAtlantic)

        return list(pacific & atlantic)
                    








