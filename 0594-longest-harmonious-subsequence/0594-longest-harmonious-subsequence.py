class Solution:
    def findLHS(self, nums: List[int]) -> int:
        i=0
        j=1
        nums.sort()
        ans=0
        while (j<len(nums)):
            if nums[j]-nums[i]<1:
                j+=1
            elif nums[j]-nums[i]==1:
                j+=1
                ans=max(ans,j-i)
            else:
                i+=1
        return ans