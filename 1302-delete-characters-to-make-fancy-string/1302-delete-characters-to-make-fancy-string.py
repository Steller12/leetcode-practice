class Solution:
    def makeFancyString(self, s: str) -> str:
        count=1
        ans=s[0]
        for i in range(1,len(s)):
            if s[i]==ans[-1]:
                count=count+1
                if count<3:
                    ans=ans+s[i]
            else:
                count=1
                ans=ans+s[i]
        return ans
