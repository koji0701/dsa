class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #standard union find, init the nodes as disjoint sets
        parents = [i for i in range(n)] 

        #our return value, number of disjoint sets
        groups = n

        #standard template union find func
        def union(first: int, second: int): 
            p1 = find(first)
            p2 = find(second) 

            nonlocal groups
            if p1 != p2: 
                parents[p1] = p2

                #unique to this problem
                #as we combine sets, there's less total disjoint sets
                #after combining all edges, this equals the number of groups
                groups -= 1
        
        #standard template find func (iterative)
        def find(node: int): 
            cur = node

            while cur != parents[cur]: 
                #path compression
                parents[cur] = parents[parents[cur]]
                cur = parents[cur]
            
            return cur

        for a,b in edges: 
            union(a,b)
        return groups