class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum=0
        for i in nums:
            maximum|=i
        def helper(i,curr):
            if i==len(nums):
                return 1 if curr==maximum else 0
            return helper(i+1,curr|nums[i])+helper(i+1,curr)
        return helper(0,0)