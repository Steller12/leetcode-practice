class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            c=0
            while nums[i]:
                nums[i]=nums[i]//10
                c+=1
            if c%2==0:
                ans+=1
        return ans
