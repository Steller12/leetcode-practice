class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=-1
        for i,j in d.items():
            if i==j:
                ans=max(ans,i)
        return ans