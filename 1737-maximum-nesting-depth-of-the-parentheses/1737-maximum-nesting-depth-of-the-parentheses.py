class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        temp=0
        for i in s:
            if i=='(':
                temp+=1
            elif i==')':
                ans=max(temp,ans)
                temp-=1
            else:
                continue
        return ans