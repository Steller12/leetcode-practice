class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            c=math.floor(math.log10(nums[i]))+1
            if c%2==0:
                ans+=1
        return ans
