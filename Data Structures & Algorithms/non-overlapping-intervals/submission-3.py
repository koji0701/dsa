class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        i = 0 
        prevEnd = -99999 #prev ending time thats in our new interval list
        rv = 0
        while i < len(intervals): 
            if intervals[i][0] < prevEnd: 
                #start of cur is less than end of prev, del this one 
                rv += 1 
            
            else: 
                prevEnd = intervals[i][1] #include this interval 
            
            i += 1
        return rv