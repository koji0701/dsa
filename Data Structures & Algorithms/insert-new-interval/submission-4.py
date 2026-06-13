class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rv = []
        newStart, newEnd = newInterval
        i = 0 

        #can check the end of each interval against the new start 
        #since the intervals are nonoverlapping originally 
        #meaning that the end of the prev < start of the cur 
        while i < len(intervals) and intervals[i][1] < newStart: 
            rv.append(intervals[i])
            i += 1
        
        #i is on the interval left of newInterval 
        #you need to meerge everything that newInterval swallows 
        #since newInterval can impcat like as many intervals 

        while i < len(intervals) and intervals[i][0] <= newEnd: 
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i +=1 
        rv.append(newInterval)

        #fill rest of them 
        rv += intervals[i:]
        return rv