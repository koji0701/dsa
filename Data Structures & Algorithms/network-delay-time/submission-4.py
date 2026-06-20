class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = {}

        for fro, to, time in times: 
            if fro not in mp: 
                mp[fro] = []
            mp[fro].append((time, to))

        pq = []
        heapq.heapify(pq)

        heapq.heappush(pq, (0,k))
        seen = set()
        time = pq[0][0]

        while pq: 
            tim, to = heapq.heappop(pq) 
            if to in seen: 
                continue 
            
            seen.add(to) 
            time = tim
            if to not in mp: continue 

            for nTim, nTo in mp[to]: 
                heapq.heappush(pq, (time + nTim, nTo))

        if len(seen) != n:
            print(len(seen)) 
            return -1
        return time


