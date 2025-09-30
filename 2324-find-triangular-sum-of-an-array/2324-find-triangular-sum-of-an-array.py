class Solution:
    def triangularSum(self, nums: List[int]) :
        newnums=nums
        while len(newnums)>1:
            temp=[]
            for i in range(len(newnums)-1):
                x=(newnums[i]+newnums[i+1])%10
                temp.append(x)
            newnums=temp
        return sum(newnums)
            