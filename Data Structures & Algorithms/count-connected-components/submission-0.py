#bfs or union find (optimal)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        mp = {i:[] for i in range(n)}
        groups = 0
        for a, b in edges: 
            mp[a].append(b)
            mp[b].append(a)
        
        def bfs(node: int): 
            queue = deque()
            queue.append(node) 
            while queue: 
                cur = queue.popleft()
                for nei in mp[cur]: 
                    if nei not in seen: 
                        queue.append(nei)
                        seen.add(nei)

        for i in range(n): 
            if i in seen: 
                continue 
            bfs(i)
            groups += 1
        
        return groups
