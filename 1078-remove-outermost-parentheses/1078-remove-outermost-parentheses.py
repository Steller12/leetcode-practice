class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp=0
        ans=''
        for i in s:
            if i==')':
                temp-=1
            if temp!=0:
                ans+=i
            if i=='(':
                temp+=1
        return ans