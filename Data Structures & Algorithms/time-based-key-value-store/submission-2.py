'''
hashmap at each node
- nodes containing a hashmap consisting of the key:vals

SortedDict 
- {key : SortedArray [(timestamp, key)]} #sortedarray sorts by first tuple

binary search the sorted dict by timestamp
- only binary search starting by going left (less time), 
    since if set after it doesnt matter

alt idea: intervals? (start=timestamp, end=99999 until next timestamp)
'''

from sortedcontainers import SortedList
class TimeMap:
    def __init__(self):
        self.mp = {} #key : SortedArray [(timestamp, key)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp: 
            self.mp[key] = SortedList()
        self.mp[key].add((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp: 
            return ""

        lis = self.mp[key]

        low = 0
        high = len(lis)
        mid = (high-low)//2 + low

        #looking for nums[i] <= target (right bound)

        #need to commit this to memory
        while low < high: 
            mid = (high-low)//2 + low
            if lis[mid][0] <= timestamp: 
                low = mid + 1
            else: 
                high = mid
        
        #final check, is the smallest timestamp larger than timestamp
        if lis[low-1][0] > timestamp:
            return ""
        return lis[low-1][1]















