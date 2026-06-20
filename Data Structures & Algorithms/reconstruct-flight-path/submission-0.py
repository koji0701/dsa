class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True) 
        #sorts by the from first (which doesnt matter since we add left to right)
        #then all the to's are sorted as the tiebreaker 
        mp = {}
        for fro, to in tickets: 
            if fro not in mp: 
                mp[fro] = []
            mp[fro].append(to) 
        
        stack = deque() 
        stack.append("JFK")
        order = []
        while stack: 
            cur = stack[-1]
            if cur in mp and len(mp[cur]) > 0: 
                stack.append(mp[cur].pop())
            else: 
                order.append(cur) 
                stack.pop()
        
        return order[::-1]