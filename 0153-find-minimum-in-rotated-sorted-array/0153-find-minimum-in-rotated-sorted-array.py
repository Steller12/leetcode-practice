class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        return nums[l]
