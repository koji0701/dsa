class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0

        for v in s: 
            if v == "*": 
                minOpen -=  1
                maxOpen += 1
            elif v == "(": 
                minOpen += 1
                maxOpen += 1
            else: 
                minOpen -= 1
                maxOpen -= 1

            if maxOpen < 0: 
                return False 
            minOpen = max(0, minOpen)
        
        print(minOpen, maxOpen)
        return minOpen == 0




