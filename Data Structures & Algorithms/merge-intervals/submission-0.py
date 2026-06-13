class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        rv = []
        intervals.sort() #sort by start
        i = 1
        rv.append(intervals[0])

        while i < len(intervals): 
            start, end = intervals[i][0], intervals[i][1]
            if start <= rv[-1][1]: 
                rv[-1][1] = max(end, rv[-1][1])
            else: 
                rv.append(intervals[i])
            i += 1
        
        return rv