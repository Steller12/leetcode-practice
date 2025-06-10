class Solution:
    def maxDifference(self, s: str) -> int:
        f=[0]*26
        for i in s:
            temp=ord(i)-ord('a')
            f[temp]+=1
        o=0
        e=float('inf')
        for i in f:
            if i==0:
                continue
            if i%2==0:
                e=min(e,i)
            else:
                o=max(o,i)
        return (o-e)