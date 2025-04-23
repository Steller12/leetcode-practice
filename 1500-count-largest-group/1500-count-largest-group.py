class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            sum=0
            temp=i
            while temp>0:
                sum=sum+temp%10
                temp=temp//10
            if sum in d.keys():
                d[sum]+=1
            else:
                d[sum]=1
        d2={}
        for i in d.values():
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        return d2[max(d2.keys())]