class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s=0
            a=nums[i]
            while a!=0:
                s=s+(a%10)
                a=a//10
            nums[i]=s
        return min(nums)