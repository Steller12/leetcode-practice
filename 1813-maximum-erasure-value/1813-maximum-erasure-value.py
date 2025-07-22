class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i=0
        ans=0
        current=0
        flag=set()
        for j in nums:
            while j in flag:
                current-=nums[i]
                flag.remove(nums[i])
                i+=1
            current+=j
            flag.add(j)
            ans=max(ans,current)
        return ans
