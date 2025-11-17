class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        curr=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr=curr+1
                ans=max(ans,curr)
            else:
                curr=0
        return ans
