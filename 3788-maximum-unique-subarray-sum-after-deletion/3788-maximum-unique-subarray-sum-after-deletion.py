class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx <= 0:
            return mx
        unique = set(nums)
        return sum(num for num in unique if num > 0)