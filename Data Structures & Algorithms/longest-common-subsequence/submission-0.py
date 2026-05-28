class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longestSubsequence = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for t2 in range(len(text2)): 
            for t1 in range(len(text1)): 
                if text1[t1] == text2[t2]: 
                    longestSubsequence[t2+1][t1+1] =  longestSubsequence[t2][t1] + 1
                else: 
                    longestSubsequence[t2+1][t1+1] = max(longestSubsequence[t2][t1+1], longestSubsequence[t2+1][t1])
        
        return longestSubsequence[-1][-1]