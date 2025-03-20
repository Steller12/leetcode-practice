class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        x=1
        for i in range(len(nums)):
            if i==0:
                ans.append(x)
            else:
                x=x*nums[i-1]
                ans.append(x)
        x=1
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                continue
            else:
                x=x*nums[i+1]
                ans[i]=ans[i]*x
        return ans