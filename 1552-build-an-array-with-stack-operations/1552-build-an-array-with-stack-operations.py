class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        x=0
        for i in range(1,n+1):
            ans.append("Push")
            if i==target[x]:
                x+=1
                if x==len(target):
                    break
            else:
                ans.append("Pop")
        return ans
            