class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans=1
        nums.sort()
        temp=0
        for i in range(len(nums)):
            if nums[i]-nums[temp]>k:
                ans+=1
                temp=i
        return ans