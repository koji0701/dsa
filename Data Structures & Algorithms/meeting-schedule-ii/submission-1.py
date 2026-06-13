"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        endTimes = []
        heapq.heapify(endTimes)

        maxRooms = 0 
        intervals.sort(key=lambda x: x.start)
        
        for interval in intervals: 
            while len(endTimes) > 0 and endTimes[0] <= interval.start: 
                heapq.heappop(endTimes) 
            
            heapq.heappush(endTimes, interval.end) 
            maxRooms = max(maxRooms, len(endTimes))
            print(endTimes) 
        
        return maxRooms

            








