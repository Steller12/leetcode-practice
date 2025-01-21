class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = 0
        maxLen=0
        lastRem=0
        for i,v in enumerate(s):
            if v in seen and lastRem <= seen[v]:
                length = i-(seen[v]+1)+1
                lastRem = seen[v]
                seen[v]=i
            else:
                seen[v]=i
                length+=1
            
            if length > maxLen:
                maxLen=length
        return maxLen