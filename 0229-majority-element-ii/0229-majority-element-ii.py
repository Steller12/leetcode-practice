class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        for j,i in d.items():
            if i>n:
                res.append(j)
        return res