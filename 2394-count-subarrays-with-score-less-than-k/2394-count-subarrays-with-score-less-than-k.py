class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        s=0
        x=0
        l=0
        ans=0
        for r in range(len(nums)):
            s=s+nums[r]
            while l<=r and s*(r-l+1)>=k:
                s=s-nums[l]
                l=l+1
            ans+=r-l+1
        return ans