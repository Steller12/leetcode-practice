class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans=0
        x=0
        y=0
        for i in range(len(s)):
            if s[i]=="N":
                y+=1
            elif s[i]=="S":
                y-=1
            elif s[i]=="E":
                x+=1
            else:
                x-=1
            dist=abs(x)+abs(y)
            ans=max(ans, min(dist+k*2,i+1))
        return ans