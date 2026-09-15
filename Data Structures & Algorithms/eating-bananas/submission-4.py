class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(val) -> bool: 
            hours = 0
            for p in piles:
                hours += (p + val - 1) // val   # ceil(p / val)
                if hours > h:                   # early exit
                    return False
            return hours <= h

        low = 1 
        high = max(piles) 
        #binary search for the lowest value of k 
        mid = 0
        k = high 

        while low < high: 
            mid = (high-low) // 2 + low 
            if isValid(mid): 
                k = mid 
                high = mid
            else: 
                low = mid + 1
        
        return k






