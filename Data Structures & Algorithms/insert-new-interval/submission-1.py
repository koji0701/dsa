class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        rv = []
        i = 0 

        while i< len(intervals) and intervals[i][1] < newInterval[0]: 
            rv.append(intervals[i])
            i += 1
        
        #merge here 

        insertion = [newInterval[0], newInterval[1]]
        while i< len(intervals) and intervals[i][0] <= insertion[1]: 
            insertion[0] = min(insertion[0], intervals[i][0])
            insertion[1] = max(insertion[1], intervals[i][1])
            i += 1
        
        rv.append(insertion) 
        
        #add the remaining 
        while i < len(intervals): 
            rv.append(intervals[i])
            i += 1


        print(rv) 
        return rv