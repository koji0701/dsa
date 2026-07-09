class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1 
            
        composite = 0 
        pos = 0 
        rv = 0

        #if composite score ever goes below 0, it means anything before 
        #that point would not have been able to go above 0 (since running sum)
        #because of that, u can move the potential rv to be past the pos 

        while pos < len(gas): 
            composite += gas[pos] - cost[pos]
            if composite < 0: 
                composite = 0 
                rv = pos + 1
            
            pos += 1
        
        return rv



