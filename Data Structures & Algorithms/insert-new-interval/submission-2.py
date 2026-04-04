class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEdge = newInterval 
        i = 0 
        #get to insertion point 
        rv = []
        while i < len(intervals) and intervals[i][1] < newStart: 
            rv.append(intervals[i])
            i += 1 
        
        #make insertion, will insert the [newStart, newEdge]

        while i < len(intervals) and intervals[i][0] <= newEdge: 
            newEdge = max(intervals[i][1], newEdge)
            newStart = min(intervals[i][0], newStart)
            i += 1
        rv.append([newStart, newEdge])

        #add the rest 
        while i<len(intervals): 
            rv.append(intervals[i])
            i += 1
        
        return rv