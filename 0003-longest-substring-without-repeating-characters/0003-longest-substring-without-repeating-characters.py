class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=""
        m=0
        for i in s:
            while i in n:
                n=n[1:]
            n=n+i
            m=max(m,len(n))
        return m