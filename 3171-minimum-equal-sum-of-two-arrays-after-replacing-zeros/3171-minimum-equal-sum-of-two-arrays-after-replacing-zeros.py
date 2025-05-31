class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeroes1 = nums1.count(0)
        zeroes2 = nums2.count(0)

        if zeroes1 == 0 and sum2+zeroes2 > sum1:
            return -1
        if zeroes2 == 0 and sum1+zeroes1 > sum2:
            return -1

        minSum = max(sum1+zeroes1, sum2+zeroes2)
        return minSum  