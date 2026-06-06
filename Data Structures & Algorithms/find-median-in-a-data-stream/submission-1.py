#2 heaps, one min one max. max heap for lower half of the numbers
#min heap for the upper half 
#top of min and/or max heap is the median


class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify_max(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if len(self.right) > 0 and num > self.right[0]: 
            heapq.heappush(self.right, num)
            self._rebalance()
        else: 
            heapq.heappush_max(self.left, num) 
            self._rebalance()



    def findMedian(self) -> float:

        if len(self.right) == 0: 
            return self.left[0]
        elif len(self.left) == 0: 
            return self.right[0]

        if len(self.right) > len(self.left): 
            return self.right[0]
        else: 
            return (self.right[0] + self.left[0]) / 2.0
            
    
    def _rebalance(self): 
        while len(self.left) > len(self.right):  
            top = heapq.heappop_max(self.left)
            heapq.heappush(self.right, top)
            
        while len(self.right) > len(self.left) + 1: 
            top = heapq.heappop(self.right)
            heapq.heappush_max(self.left, top)
        







