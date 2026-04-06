#union find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        groups = n
        def union(first: int, second: int): 
            p1 = find(first)
            p2 = find(second) 
            nonlocal groups
            if p1 != p2: 
                parents[p1] = p2
                groups -= 1
        
        def find(node: int): 
            cur = node
            while cur != parents[cur]: 
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]
            
            return cur

        
        for a,b in edges: 
            union(a,b)
        return groups