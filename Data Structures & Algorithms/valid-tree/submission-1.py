'''
def of tree
- one root node 
- num of edges = num of nodes - 1

union find algo, auto detects for if all nodes can be reached + acyclic
'''
#union find

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False 
        
        parents = [i for i in range(n)]

        def union(i: int, j: int): 
            iRep = find(i) 
            jRep = find(j) 

            parents[jRep] = iRep
        
        def find(node: int) -> int: 
            if node == parents[node]: 
                return node 
            
            representative = find(parents[node])
            return representative

        for a, b in edges: 
            union(a,b) 
        
        #if theres one representative for the entire thing, its tree
        root = find(parents[0])
        for elem in parents: 
            cur = find(elem) 
            if cur != root: 
                return False 
        return True



