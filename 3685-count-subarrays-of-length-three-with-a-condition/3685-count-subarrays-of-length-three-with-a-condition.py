class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)-2):
            x=nums[i:i+3]
            if x[0]+x[-1]==x[1]/2:
                ans=ans+1
        return ans