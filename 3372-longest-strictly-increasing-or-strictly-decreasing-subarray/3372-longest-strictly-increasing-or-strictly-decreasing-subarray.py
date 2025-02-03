class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length=0
        for i in range(len(nums)):
            c=1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[j-1]:
                    c=c+1
                else:
                    break
            max_length=max(max_length,c)
        for i in range(len(nums)):
            c=1
            for j in range(i+1,len(nums)):
                if nums[j]<nums[j-1]:
                    c=c+1
                else:
                    break
            max_length=max(max_length,c)
        return max_length