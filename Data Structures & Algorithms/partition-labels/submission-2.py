class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastPos = {}
        for i, v in enumerate(s):
            lastPos[v] = i 

        left = 0 
        right = 1
        cur = 0

        rv = []

        while right < len(s) and left < len(s): 
            leftLetter = s[left]
            right = lastPos[leftLetter]
            
            while cur < right: 
                curLetter = s[cur]
                right = max(right, lastPos[curLetter])
                cur += 1
            
            rv.append(cur - left + 1)
            left = cur+1
        
        return rv
        
        



