class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        a=[]

        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1

        for key,value in d.items():
            a.append([value,key])

        a=sorted(a)

        while len(ans)<k:
            ans.append(a.pop()[1])

        return ans
