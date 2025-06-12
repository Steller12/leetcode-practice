class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans=-float('inf')
        for i in range(1,len(nums)):
            ans=max(ans,(nums[i-1])-nums[i])
        ans=max(ans,nums[-1]-nums[0])
        return ans
