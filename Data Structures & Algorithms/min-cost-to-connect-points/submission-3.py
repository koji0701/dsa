class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #construct all edges in sorted order 
        edges = []
        parents = [i for i in range(len(points))]
        heapq.heapify(edges)

        for j in range(len(points)): 
            x, y = points[j]
            for i in range(j+1, len(points)): 
                nx, ny = points[i]
                dist = abs(x-nx) + abs(y-ny) 
                heapq.heappush(edges, (dist, i, j))            

        cost = 0

        def union(i: int, j: int): 
            nonlocal parents

            root_i = find(i) 
            root_j = find(j)
            parents[root_i] = root_j
            
        
        def find(i: int) -> int: 
            nonlocal parents
            while i != parents[i]: 
                parents[i] = parents[parents[i]]
                i = parents[i]
            return i


        while edges: 
            dist, i, j = heapq.heappop(edges) 
            #print("dist",dist,"i: ",i,"j:",j)
            while edges and find(i) == find(j):
                dist, i, j = heapq.heappop(edges) 
                #print("popping", "dist",dist,"i: ",i,"j:",j)
            

            if find(i) != find(j):
                cost += dist 
                union(i, j)

        return cost
