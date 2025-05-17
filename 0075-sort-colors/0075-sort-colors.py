class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        n=len(nums)
        for i in nums:
            if i==0:
                zero+=1
            if i==1:
                one+=1
        for i in range(0,zero):
            nums[i]=0
        for i in range(zero,zero+one):
            nums[i]=1
        for i in range(zero+one,n):
            nums[i]=2
        return nums