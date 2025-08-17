class Solution:
    def maximum69Number (self, num: int) -> int:
        temp=str(num)
        ans=''
        count=1
        for i in range(len(temp)):
            if temp[i]=='6' and count>0:
                ans=ans+'9'
                count-=1
            else:
                ans=ans+temp[i]
        return int(ans)