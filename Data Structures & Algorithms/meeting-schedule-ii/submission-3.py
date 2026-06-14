"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #alt: general sweep line algorithm
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #step 1: flatten intervals 
        flat = [None] * (len(intervals) * 2)

        for i in range(len(intervals)): 
            flat[i*2] = (intervals[i].start, 1)
            flat[i*2+1] = (intervals[i].end, -1)

        #step 2: sort the flattened intervals 
        flat.sort()

        #step 3: +1 for arrivals, -1 for departures. keep track of max 
        maxRooms = 0 
        curRooms = 0 

        for _, val in flat: 
            curRooms += val 
            maxRooms = max(maxRooms, curRooms) 
        
        return maxRooms








