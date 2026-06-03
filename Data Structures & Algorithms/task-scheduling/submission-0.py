class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0 
        heap = []
        processing = deque()  #(time unlocked, freq, task)

        heapq.heapify_max(heap)

        freqMap = {} 
        for task in tasks: 
            if task not in freqMap: 
                freqMap[task] = 0 
            
            freqMap[task] += 1


        for task, fr in freqMap.items(): 
            heapq.heappush_max(heap, fr)
        
        print(heap) 

        while heap: 
            fr = heapq.heappop_max(heap) 
            nf = fr - 1 

            if nf > 0: 
                processing.append((time+n, nf))

            if processing and processing[0][0] <= time: 
                newTime, newF = processing.popleft() 
                heapq.heappush_max(heap, newF)


            if len(heap) == 0 and len(processing) != 0: 
                newTime, newF = processing.popleft() 
                time = newTime 
                heapq.heappush_max(heap, newF)

            time += 1
        
        return time 
            

