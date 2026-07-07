class Solution:
    def checkValidString(self, s: str) -> bool:
        #for string to be valid, the num of left parenthesis matching right parenthesis 
        #must equal 0 

        #there is an interval of possibilities due to the wildcard, which can be 
        #empty, left, right 

        #so, the intereval just needs to contain 0
        #keep track of min and max 

        minLeft = 0 
        maxLeft = 0 

        for v in s: 
            if v == "*": 
                minLeft = max(0, minLeft -1 ) 
                maxLeft += 1
            elif v == "(": 
                minLeft += 1
                maxLeft += 1
            else: 
                minLeft -= 1
                maxLeft -= 1
            
            if maxLeft < 0: 
                return False 
        
        return minLeft <= 0

