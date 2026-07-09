class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #two subsequences pattern, construct a s*t grid 

        grid = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        print(s)
        print(t) 
        print(grid) 

        #there is 1 way to make base cases 

        grid[0] = [1 for _ in range(len(s)+1)]

        

        for t1 in range(1, len(grid)): 
            for s1 in range(1, len(grid[0])): 
                print("reached", s1, t1, len(s), len(t))
                if s[s1-1] == t[t1-1]: 
                    grid[t1][s1] = grid[t1-1][s1-1] + grid[t1][s1-1]
                else: 
                    grid[t1][s1] = grid[t1][s1-1]
        
            
        print(grid) 
        return grid[-1][-1]


