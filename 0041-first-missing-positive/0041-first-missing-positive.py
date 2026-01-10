class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = set(nums)
        z = 1
        while z in x:
            z += 1
        return z