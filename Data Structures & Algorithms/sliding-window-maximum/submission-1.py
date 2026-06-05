class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() 
        rv = []
        
        for i in range(len(nums)): 
            #outside of window, kick it out
            if q and q[0] <= i-k: 
                q.popleft() 
            
            while q and nums[i] >= nums[q[-1]]: 
                q.pop() 
            
            q.append(i)

            #if we have a window
            if i >= k-1: 
                rv.append(nums[q[0]])
        
        return rv
