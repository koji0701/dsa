class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by ending
        intervals.sort(key=lambda x: x[1])

        i = 0
        rv= 0
        prevEnd = -999999
        while i < len(intervals): 
            if intervals[i][0] < prevEnd: 
                rv += 1
                #i += 1
            else:
                prevEnd = intervals[i][1]
            i += 1
        return rv