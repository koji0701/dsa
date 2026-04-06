'''
union find 
- something to do with the rank optimization 
        that'll catch where cycle is 

- rank array keeps track of how many children a node has
    - each index is a representative
    - set to -1 if not a rep


cycle detection: 
- when iterating the unions 
    - if a node already has a parent thats not itself, and is asked to relocate, 
    then this is cyclical? 
    - yes
    - ordering of this determined by the rank optimization
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for i in range(len(edges)): 
            edges[i][0] -= 1
            edges[i][1] -= 1
            


        n = len(edges) 
        parents = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        redundant = []
        def union(first: int, second: int): 
            p1 = find(first) 
            p2 = find(second) 
            if p1 == p2: 
                nonlocal redundant
                redundant = [first+1, second+1]

            if rank[p1] < rank[p2]: 
                parents[p1] = p2
            elif rank[p2] < rank[p1]: 
                parents[p2] = p1
            else: 
                parents[p1] = p2
                rank[p2] += 1
        
        
        def find(node: int): 
            cur = node 
            while parents[cur] != cur: 
                parents[cur] = parents[parents[cur]] #path compress
                cur = parents[cur]

            return cur


        for a,b in edges: 
            union(a,b) 

        return redundant




