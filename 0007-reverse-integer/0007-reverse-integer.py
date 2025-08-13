class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        temp=abs(x)
        while temp:
            temp2=temp%10
            temp=temp//10
            ans=(ans*10)+temp2
        if ans>((2**31) - 1) or ans<((-2)**31):
            return 0
        else:
            if x<0:
                return ans*(-1)
            else:
                return ans
