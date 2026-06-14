"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #alt: sweep line, slightly optimized
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        i = 0
        j = 0 
        curRooms = 0 
        maxRooms = 0 

        #last end no matter is after the last start
        while i < len(intervals): 
            if starts[i] < ends[j]: 
                curRooms += 1
                i += 1
            else: 
                curRooms -= 1
                j +=1 

            maxRooms = max(maxRooms, curRooms) 
        
        return maxRooms








