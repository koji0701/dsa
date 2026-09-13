class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) 
        for num in nums: 
            freq[num] += 1

        heap = [] #(freq, elem)
        heapq.heapify(heap) 

        for num, fr in freq.items(): 
            heapq.heappush(heap ,(fr, num))
            if len(heap) > k: 
                heapq.heappop(heap)
        
        rv = []
        for elem in heap: 
            rv.append(elem[1])
        
        return rv