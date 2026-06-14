class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #construct grid of (empty+s1) x (empty+s2) 
        #rows: letters of s1, 
        #cols: letters of s2
        #values: True for reachable, False for not reachable
        #u transition once at a time, by moving right or down
        #base cases: -1's and 1's on first row and col (covered by empty)

        if len(s3) != len(s1)+len(s2): 
            return False

        grid = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        # 2. Base Case: Double empty strings
        grid[0][0] = True

        # 3. Fill the top row (s1 is empty, only using s2)
        for j in range(1, len(s2) + 1):
            # Only True if the current letter matches AND the previous cell was True
            if grid[0][j-1] and s2[j-1] == s3[j-1]:
                grid[0][j] = True

        # 4. Fill the left column (s2 is empty, only using s1)
        for i in range(1, len(s1) + 1):
            # Only True if the current letter matches AND the cell above was True
            if grid[i-1][0] and s1[i-1] == s3[i-1]:
                grid[i][0] = True
        
        for i in range(1, len(grid)): 
            for j in range(1, len(grid[0])): 
                if grid[i][j-1] and s2[j-1] == s3[i+j-1]: 
                    grid[i][j] = True
                if s1[i-1] == s3[i+j-1] and grid[i-1][j]: 
                    grid[i][j] = True

        return grid[-1][-1]
        





